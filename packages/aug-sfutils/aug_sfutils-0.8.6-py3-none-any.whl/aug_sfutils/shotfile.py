import os, logging, traceback
from struct import unpack, pack
import numpy as np
from aug_sfutils import sfmap, sfobj, str_byt
from aug_sfutils.sfmap import oid, olbl, ostruc, oattr, header_sfmt

fmt = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s: %(message)s', '%H:%M:%S')

logger = logging.getLogger('aug_sfutils.shotfile')

if len(logger.handlers) == 0:
    hnd = logging.StreamHandler()
    hnd.setFormatter(fmt)
    logger.addHandler(hnd)

logger.setLevel(logging.INFO)
#logger.setLevel(logging.DEBUG)

PPGCLOCK = [1e-6, 1e-5, 1e-4, 1e-3]
LOGICAL  = sfmap.typeMap('descr', 'SFfmt', 'LOGICAL')


def getChunk(fname, start, length):
    """Reads the requested byteblock from the binary shotfile"""

    rdata = None
    with open(fname, 'rb') as f:
        f.seek(start)
        rdata = f.read(length)
    return rdata


def param_length(param):
    """Determines the byte length of a Parameter"""

    parmlen = 16 # ParName(=key), unit, dfmt, n_items
    dfmt = param.dataFormat
    bytlen = param.n_items * sfmap.typeLength(dfmt)
    parmlen += 8 * ( (bytlen + 13)//8 )

    return parmlen


def parset_length(pset_d):
    """Determines the byte length of a ParameterSet"""

    psetlen = 0
    for param in pset_d.values():
        psetlen += param_length(param)

    return psetlen


def par2byt(pname, param):
    """Converts the parameter data into bytes"""

    dfmt = param.dataFormat
    n_items = param.n_items

    if dfmt in sfmap.fmt2len.keys(): # char variable
        dlen = sfmap.fmt2len[dfmt]
        bytlen = n_items * dlen
        dj0 = 8 * ( (bytlen + 9)//8 ) 
    elif dfmt in sfmap.dtf['SFfmt'].values: # number
        sfmt = sfmap.typeMap('SFfmt', 'struc', dfmt)
        type_len = np.dtype(sfmt).itemsize
        val_len = n_items + 2
        bytlen = val_len * type_len
        dj0 = str_byt.next8(bytlen)
    blen = 16 + dj0
    byt = bytearray(blen)
    byt[  :  8] = str_byt.to_byt(pname.ljust(8))
    byt[ 8: 16] = pack('>4h', param.physunit, dfmt, n_items, param.status)
    if dfmt in sfmap.fmt2len.keys(): # character variable
        byt[16: 17] = param.dmin
        byt[17: 18] = param.dmax
        param2 = np.atleast_1d(param)
        for jitem in range(n_items):
            if len(param[jitem]) > 0:
                byt[18 + jitem*dlen: 18 + (jitem+1)*dlen] = param2[jitem].ljust(dlen)
    elif dfmt in sfmap.dtf['SFfmt'].values: # number
        if dfmt == LOGICAL: # logical, bug if n_items > 1?
            byt[16: 22] = pack('>?2x?1x?', param.dmin, param.dmax, param)
        else:
            byt[16: 16+2*type_len] = pack('>2%s' %sfmt, param.dmin, param.dmax)
            param2 = np.atleast_1d(param)
            byt[16: 16 + (n_items+2)*type_len] = pack('>%d%s' %(2+n_items, sfmt), param.dmin, param.dmax, *param2)
    return byt


class SHOTFILE(dict):


    def __init__(self, sfpath, sffull=None):

        self.__dict__ = self

        if not os.path.isfile(sfpath) and sffull is None:
            logger.error('Shotfile %s not found', sfpath)
            return None

        if sffull is None: # read shotfile if no SFobj is input
            self.shotfilePath = sfpath
            self.read_sfh()
            self.set_attributes()
        else: # for SF writing
            if isinstance(sffull, dict):
                for key, val in sffull.items():
                    setattr(self, key, val)
            else:
                for key, val in sffull.__dict__.items():
                    setattr(self, key, val)
            self.shotfilePath = sfpath
            self.sfh2byte() # converts to bytes string (Shotfile content)


    def read_sfh(self, psets=True):
        """Reads a full shotfile header, including the data of ParamSets, Devices, Lists"""

        self.SFobjects = []
        self.addressMultiplier   = 1

        n_max = 1000
        n_obj = n_max
        self.objId2objName = []
        for j in range(n_max):
            sfo = SF_OBJECT(jobj=j, sfname=self.shotfilePath)
            if hasattr(sfo, 'objectType'):
                sfo.objid = j
                onam = str_byt.to_str(sfo.objectName.strip())
                if sfo.SFOtypeLabel == 'Diagnostic':
                    if n_obj == n_max: # There might be several diags objects in a SFH
                        self.shotNumber = sfo.shot
                        self.diagName   = str_byt.to_str(sfo.diag.strip())
                        n_obj = sfo.num_objs
                self.objId2objName.append(onam)
                self.SFobjects.append(sfo)
                if sfo.SFOtypeLabel == 'ADDRLEN':
                    self.addressMultiplier = sfmap.addrsizes[sfo.addrlen]
                self.__dict__[onam] = sfo
            if j >= n_obj - 1:
                break


    def set_attributes(self):
        """Sets useful context info for the entire shotfile, plus data for Lists, ParmSets, Devices"""

        for sfo in self.SFobjects:
            sfo.address *= self.addressMultiplier
            sfo.relations  = [self.objId2objName[jid] for jid in sfo.rel if jid != 65535]
            sfo.relobjects = [self.SFobjects[jid]     for jid in sfo.rel if jid != 65535]
            if hasattr(sfo, 'dataFormat'):
                if sfo.dataFormat in sfmap.dtf['SFfmt'].values:
                    sfo.dataType = sfmap.typeMap('SFfmt', 'descr', sfo.dataFormat)
            if sfo.SFOtypeLabel == 'List':
                sfo.getData()
                sfo.data = []
                for jid in sfo.data:
                    sfo.data.append(self.objId2objName[jid])
 
            elif sfo.SFOtypeLabel in ('Device', 'ParamSet'):
                sfo.getData()
                if sfo.SFOtypeLabel == 'Device':
                    if 'TS06' in sfo.data.keys(): # former get_ts06
                        ts06 = sfo.data['TS06']
                        if ts06 > 1e15:
                            sfo.ts06 = ts06

            elif sfo.SFOtypeLabel in ('Signal', 'SignalGroup'):
                for jrel, robj in enumerate(sfo.relobjects):
# check where the related timebase is
                    if robj.SFOtypeLabel == 'TimeBase':
                        shape_arr = sfo.index[::-1][:sfo.num_dims]
                        nt = robj.n_steps
                        if shape_arr.count(nt) == 1:
                            sfo.time_dim = shape_arr.index(nt)
                        sfo.timebase = robj
                        sfo.time_dim = jrel
# For data calibration
                        if sfo.phys_unit == 'counts':
                            sfo.cal_fac = robj.s_rate
# check where the related areabase is
                    elif robj.SFOtypeLabel == 'AreaBase':
                        sfo.areabase = robj
                        sfo.area_dim = jrel

#----------------
# Writing section
#----------------
    def sfh2byte(self):
        """Converts all SF objects' metadata to bytes (shotfile header content)"""

# Fill missing attributes in signle objects

        if not hasattr(self, 'SFobjects'):
            self.SFobjects = []
            for lbl, sfo in vars(self).items():
                if hasattr(sfo, 'data') or hasattr(sfo, 'SFOtypeLabel'):
                    sfo.objectName = lbl
                    sfo.setDefault()
                    self.SFobjects.append(sfo)

        self.setSIGNALS()
        objNames = [sfo.objectName for sfo in self.SFobjects]
        if 'SIGNALS' not in objNames:
            self.SFobjects.insert(1, self.SIGNALS)
        self.setSIGNALSdata()

        objName2objId = {}
        for jid, sfo in enumerate(self.SFobjects):
            objName2objId[sfo.objectName] = jid

        for jid, sfo in enumerate(self.SFobjects):
            if not hasattr(sfo, 'rel'):
                if hasattr(sfo, 'relations'):
                    sfo.rel = [objName2objId[oname] for oname in sfo.relations]
                    while len(sfo.rel) < 8:
                        sfo.rel.append(65535)
                else:
                    sfo.rel = 8*[65535] # defaulting to empty

        self.set_length_address()

        num_objs = len(self.SFobjects)
        self.SFbytes = b''
        for sfo in self.SFobjects:
            if sfo.SFOtypeLabel == 'Diagnostic':
                sfo.num_objs = num_objs
# Encode all attributes into byte strings(128)
            self.SFbytes += sfo.sfoh2byte()

# Write SIGNALS list
        self.SFbytes += self.SIGNALS.data

# Write content of ParSets
        for sfo in self.SFobjects:                
            if sfo.SFOtypeLabel == 'ParamSet':
                pset2byt = b''
                for pname, param in sfo.data.items():
                    pset2byt += par2byt(pname, param)
                self.SFbytes.ljust(sfo.address) # Ensure proper localisation
                self.SFbytes += pset2byt


    def putData(self):
        """Add data to Sf objects"""

        for sfo in self.SFobjects:
            if sfo.SFOtypeLabel in sfmap.DataObjects:
                if hasattr(sfo, 'data'):
                    sfmt  = sfmap.typeMap('SFfmt', 'struc', sfo.dataFormat)
                    sfo.data = sfo.data.astype('>%s' %sfmt)
                    if sfo.data.nbytes == sfo.length:
                        self.SFbytes = self.SFbytes.ljust(sfo.address)
                        self.SFbytes += sfo.data.tobytes(order='F')
                    else:
                        logger.error('Shape/type of %s does not match buffer length', sfo.objectName)
                        return
                else:
                    logger.warning('Missing data for object %s', sfo.objectName)


    def dumpShotfile(self):
        """Dumps Shotfile(header)"""

        sfout = self.shotfilePath
        if hasattr(self, 'SFbytes'):
            with open(sfout, 'wb') as f:
                f.write(self.SFbytes)
            logger.info('Stored binary %s' %sfout)


    def setSIGNALS(self):
        """Generates 'SIGNALS' list automatically"""

# SIGNALS list generated automatically, override input entry
        self.SIGNALS = SF_OBJECT()
        self.SIGNALS.dataFormat = sfmap.typeMap('descr', 'SFfmt', 'SHORT_INT')
        self.SIGNALS.SFOtypeLabel = 'List'
        self.SIGNALS.objectName = 'SIGNALS'


    def setSIGNALSdata(self):

        sfmt = sfmap.typeMap('SFfmt', 'struc', self.SIGNALS.dataFormat)
        objid = [jid for jid, sfo in enumerate(self.SFobjects) if sfo.SFOtypeLabel in sfmap.DataObjects]
        self.SIGNALS.nitems = len(objid)
        self.SIGNALS.data = pack('>%d%s' %(self.SIGNALS.nitems, sfmt), *objid)
        self.SIGNALS.length = self.SIGNALS.nitems*2
        self.SIGNALS.address = len(self.SFobjects)*128
        self.SIGNALS.setDefault()


    def set_length_address(self):
        """Recalculates the address and length of SF objects, recreating the 'SIGNALS' list consistently"""

# ParSets

        len_psets = 0
        for jid, sfo in enumerate(self.SFobjects): # sequence not important
            if sfo.SFOtypeLabel == 'ParamSet':
                sfo.length = parset_length(sfo.data)
                len_psets += sfo.length

# Set lengths and addresses

        addr_diag = self.SIGNALS.address + self.SIGNALS.length + len_psets
        par_addr  = self.SIGNALS.address + self.SIGNALS.length 
        addr_diag = str_byt.next8(addr_diag)
        par_addr  = str_byt.next8(par_addr)

        addr = addr_diag

        for sfo in self.SFobjects:
            SFOlbl = sfo.SFOtypeLabel
            if hasattr(sfo, 'dataFormat'):
                type_len = sfmap.typeLength(sfo.dataFormat)
            else:
                type_len = 0

            if SFOlbl == 'Diagnostic':
                sfodiag = sfo
                sfo.address = addr
            elif SFOlbl == 'List':
                if sfo.objectName == 'SIGNALS':
                    for key, val in self.SIGNALS.__dict__.items():
                        setattr(sfo, key, val)
                    addr = addr_diag
            elif SFOlbl in ('Device', 'ParamSet'):
                sfo.address = par_addr
                par_addr += sfo.length
            elif SFOlbl in sfmap.DataObjects:
                sfo.length = sfmap.objectLength(sfo)
                sfo.address = addr
                addr += str_byt.next8(sfo.length)
            else:
                continue

        sfodiag.length = addr + sfo.length + addr_diag



class SF_OBJECT:
    """Reads/writes the metadata of a generic single object (sfo) of a Shotfile from/to the SFH's 128byte string.
    To fetch the corresponding data, call getData()"""


    def __init__(self, jobj=None, sfname=None):


        if sfname is not None:
            self.sfname = sfname
            self.read_sfoh(jobj)

    
    def read_sfoh(self, jobj):

        byte_str = getChunk(self.sfname, jobj*128, 128)

        objnam, self.objectType, self.level, self.status, self.errcode, *rel, \
            self.address, self.length, val, descr = unpack(header_sfmt, byte_str)

        self.objectName = str_byt.to_str(objnam)
        if not self.objectName:
            logger.error('Error: empty object name')
            return
        self.rel = list(rel)
        self.descr = str_byt.to_str(descr.strip())

        logger.debug('%s %d %d', self.objectName, self.address, self.length)
        logger.debug(self.descr)

        if self.objectType in olbl.keys():
            self.SFOtypeLabel = olbl[self.objectType]
            sfmt = ostruc[self.SFOtypeLabel]
        else:
            sfmt = None
            self.SFOtypeLabel = 'Unknown'

# Read SFheader, plus data for Lists, Devices, ParSets
        SFOlbl = self.SFOtypeLabel
        SFOtup = unpack(sfmt, val)
        for jattr, SFOattr in enumerate(oattr[SFOlbl]):
            setattr(self, SFOattr, SFOtup[jattr])

        if SFOlbl == 'ParamSet':
            self.calibration_type = sfmap.calibLabel[self.cal_type]
        elif SFOlbl in ('SignalGroup', 'Signal'):
            self.index = [self.index1, self.index2, self.index3, self.index4]
            if self.physunit in sfmap.unitLabel.keys():
                self.phys_unit = sfmap.unitLabel[self.physunit]
            else:
                logger.warning('No phys. unit found for object %s, key=%d', self.objectName, self.physunit)
                self.phys_unit = ''
        elif SFOlbl == 'TimeBase':
            self.timebase_type = sfmap.tbaseLabel[self.tbase_type]
        elif SFOlbl == 'AreaBase':
            self.physunit = [self.physunit1, self.physunit2, self.physunit3]
            self.phys_unit = [sfmap.unitLabel[x] for x in self.physunit]
            self.sizes = [self.size_x, self.size_y, self.size_z]


    def getData(self, nbeg=0, nend=None):
        """Stores the data part of a SF object into sfo.data"""

        if self.SFOtypeLabel in ('ParamSet', 'Device'):
            self.getParamSet()
        elif self.SFOtypeLabel == 'List':
            self.getList()
        elif self.SFOtypeLabel in sfmap.DataObjects:
            self.getObject(nbeg=nbeg, nend=nend)


    def getList(self):
        """Stores the object IDs contained in a SF list (such as SIGNALS)"""

        buf = getChunk(self.sfname, self.address, self.length)
        sfmt = sfmap.typeMap('SFfmt', 'struc', self.dataFormat)
        self.data = unpack('>%d%s' %(self.nitems, sfmt), buf) # IDs, not labels


    def getParamSet(self):
        """Returns data and metadata of a Parameter Set.
        Called by default on SFH reading"""

        buf = getChunk(self.sfname, self.address, self.length)

        j0 = 0
        self.data = {}
        logger.debug('PS: %s, addr: %d, n_item: %d, length: %d', self.objectName, self.address, self.nitems, self.length)
        for j in range(self.nitems):
            pname = str_byt.to_str(buf[j0: j0+8])
            meta = type('', (), {})()
            meta.physunit, dfmt, n_items, meta.status = unpack('>4h', buf[j0+8:  j0+16])
            if meta.physunit in sfmap.unitLabel.keys():
                meta.phys_unit = sfmap.unitLabel[meta.physunit]
            meta.n_items = n_items
            meta.dataFormat = dfmt

            j0 += 16

            if dfmt in sfmap.fmt2len.keys(): # char variable
                dlen = sfmap.fmt2len[dfmt]
                bytlen = n_items * dlen
                meta.dmin = buf[j0  : j0+1]
                meta.dmax = buf[j0+1: j0+2]
                if len(meta.dmin) == 0:
                    meta.dmin = b' '
                if len(meta.dmax) == 0:
                    meta.dmax = b' '
                data = np.chararray((n_items,), itemsize=dlen, buffer=buf[j0+2: j0+2+bytlen])
                dj0 = 8 * ( (bytlen + 9)//8 )
                j0 += dj0
            elif dfmt in sfmap.dtf['SFfmt'].values:
                sfmt = sfmap.typeMap('SFfmt', 'struc', dfmt)
                logger.debug('Numerical par %d', dfmt)
                val_len = n_items + 2
                bytlen = val_len * np.dtype(sfmt).itemsize
                if n_items >= 0:
                    if dfmt == LOGICAL: # Logical, bug if n_items > 1?
                        meta.dmin, meta.dmax, data = unpack('>?2x?1x?', buf[j0: j0+6])
                    else:
                        data = np.ndarray((val_len, ), '>%s' %sfmt, buf[j0: j0+bytlen], order='F').copy()
                        meta.dmin = data[0]
                        meta.dmax = data[1]
                        data = np.squeeze(data[2:]) # no array if n_items=1
                dj0 = str_byt.next8(bytlen)
                j0 += dj0
            else: # faulty dfmt
                break

            self.data[pname] = sfobj.SFOBJ(data, sfho=meta)

            if j0 >= self.length:
                break


    def getObject(self, nbeg=0, nend=None):
        """Stores data part of Sig, SigGrou, TimeBase, AreaBase"""

        if hasattr(self, 'nbeg'):
           if self.nbeg == nbeg and self.nend == nend:
               return # do not re-read object if data are there already
        self.nbeg = nbeg
        self.nend = nend
        if self.SFOtypeLabel in sfmap.DataObjects:
            shape_arr = sfmap.arrayShape(self)
        else:
            logger.error('Object %s is no signal, signalgroup, timebase nor areabase, skipping')
            return None

        dfmt = self.dataFormat
        if self.SFOtypeLabel == 'TimeBase' and self.length == 0:
            if self.tbase_type == sfmap.tbaseType['PPG_prog']: # e.g. END:T-LM_END
                self.ppg_time()
            else:   # ADC_intern, e.g. DCN:T-ADC-SL
                self.data = (np.arange(self.n_steps, dtype=np.float32) - self.n_pre)/self.s_rate
        else:
            type_len = sfmap.typeLength(dfmt)
            bytlen = np.prod(shape_arr) * type_len
            if dfmt in sfmap.fmt2len.keys(): # char variable
                self.data = np.chararray(shape_arr, itemsize=type_len, buffer=getChunk(self.sfname, self.address, bytlen), order='F')
            else: # numerical variable
                sfmt = sfmap.typeMap('SFfmt', 'struc', dfmt)
                addr = self.address
# Read data only in the time range of interest
                if self.SFOtypeLabel in ('Signal', 'TimeBase', 'AreaBase') or self.time_last():
                    addr += type_len*nbeg*np.prod(shape_arr[:-1])
                    if nend is None:
                        nend = shape_arr[-1]
                    bytlen = (nend - nbeg)*np.prod(shape_arr[:-1])*type_len
                    shape_arr[-1] = nend - nbeg

                self.data = np.ndarray(shape_arr, '>%s' %sfmt, getChunk(self.sfname, addr, bytlen), order='F')


    def ppg_time(self): # Bug MAG:27204; e.g. END
        """Returns the time-array in [s] for TB of type PPG_prog"""

        nptyp = sfmap.typeMap('SFfmt', 'np', self.dataFormat)
        for robj in self.relobjects:
            if robj.SFOtypeLabel == 'Device':
                ppg = robj.data # Device/ParSet dictionary
                if not 'PRETRIG' in ppg.keys():
                    continue
                if self.n_pre > 0:
                    if ppg['PRETRIG'] > 0:
                        dt = ppg['RESOLUT'][15] * PPGCLOCK[ppg['RESFACT'][15]] + 1e-6
                    else:
                        dt = 0.
                    time_ppg = dt*np.arange(self.n_pre, dtype=nptyp) - dt*self.n_pre
                    start_phase = time_ppg[-1] + dt
                else:
                    time_ppg = []
                    start_phase = 0
                for jphase in range(16):
                    if ppg['PULSES'][jphase] > 0:
                        dt = ppg['RESOLUT'][jphase]*PPGCLOCK[ppg['RESFACT'][jphase]]
                        tb_phase = dt*np.arange(ppg['PULSES'][jphase], dtype=nptyp) + start_phase
                        time_ppg = np.append(time_ppg, tb_phase)
                        start_phase = time_ppg[-1] + dt
                if len(time_ppg) != 0:
                    self.data = time_ppg[:self.n_steps]


    def time_last(self):
        """True if SigGroup has time as last coordinate"""

        if not hasattr(self, 'time_dim'):
            return False
        else:
            return (self.time_dim == self.num_dims-1)


    def sfoh2byte(self):
        """Converts SF object attributes into a 128bytes header string"""

# val string
        SFOlbl = self.SFOtypeLabel
        sfmt = ostruc[SFOlbl]
        SFOlist = []
        for SFOattr in sfmap.oattr[SFOlbl]:
            if hasattr(self, SFOattr):
                SFOlist.append(getattr(self, SFOattr))
            else:
# String attributes
                if SFOattr in ('diag', 'hostname', 'date'):
                    SFOlist.append(b'')
# (Various) integer types
                else:
                    SFOlist.append(0)
        val = pack(sfmt, *SFOlist)

        descr = str_byt.to_byt(self.descr)
        objectName = str_byt.to_byt(self.objectName)

# Pack all SFh attributes
        sfoh_byte = pack(header_sfmt, objectName.ljust(8), self.objectType, \
            self.level, self.status, self.errcode, *self.rel, self.address, \
            self.length, val, descr.ljust(64))

        return sfoh_byte


    def setDefault(self):
        """Defaulting missing attributes whenever possible"""

        if not hasattr(self, 'objectName'):
            logger.error('Missing attribute objectName')
            return

# Some defaults in case of missing attributes

        type_err = 'SF object type not understood'
        if not hasattr(self, 'SFOtypeLabel'):
            if hasattr(self, 'objectType'):
                self.SFOtypeLabel = olbl[self.objectType]
            else:
                if not hasattr(self, 'data'):
                    logger.error(type_err)
                    return
                if self.data.ndim == 1:
                    self.SFOtypeLabel = 'Signal'      # default: Signal for 1D arrays
                elif self.data.ndim > 1:
                    self.SFOtypeLabel = 'SignalGroup' # default: SignalGroup for 2-3D arrays
                else:
                    logger.error(type_err)
                    return

        if not hasattr(self, 'objectType'):
            self.objectType = oid[self.SFOtypeLabel]

        if self.SFOtypeLabel == 'Diagnostic':
            self.diag      = str_byt.to_byt(self.objectName).ljust(4)
            self.version   = 4
            self.exp       = sfmap.expType['PRIV']
            self.diag_type = sfmap.diagType['DataAcqu']
            self.up_limit  = 256
            self.s_type    = sfmap.shotType['NormalShot']
        elif self.SFOtypeLabel == 'TimeBase':
            self.n_steps = len(self.data)
        elif self.SFOtypeLabel == 'AreaBase':
            ashape = self.data.shape
            adim = self.data.ndim
            self.size_y = 0
            self.size_z = 0
            if adim == 1:
                self.size_x = ashape[0]
            elif adim == 2:
                self.size_x, self.size_y = ashape
            elif adim == 3:
                self.size_x, self.size_y, self.size_z = ashape
            if not hasattr(self, 'n_steps'):
                self.n_steps = 1
        elif self.SFOtypeLabel in ('Signal', 'SignalGroup'):
            self.num_dims = self.data.ndim
            self.index4 = self.data.shape[0]
            if self.data.ndim > 1:
                self.index3 = self.data.shape[1]
            else:
                self.index3 = 1
            if self.data.ndim > 2:
                self.index2 = self.data.shape[2]
            else:
                self.index2 = 1
            if self.data.ndim > 3:
                self.index1 = self.data.shape[3]
            else:
                self.index1 = 1
            self.index = [self.index1, self.index2, self.index3, self.index4]
            if not hasattr(self, 'physunit'):
                if hasattr(self, 'phys_unit'):
                    self.physunit = sfmap.unitType[self.phys_unit]
                elif hasattr(self, 'unit'):
                    self.physunit = sfmap.unitType[self.unit]
                else:
                    self.physunit = 0

        if self.SFOtypeLabel in sfmap.DataObjects:
            if not hasattr(self, 'dataFormat'):
                if hasattr(self, 'data'):
                    self.dataFormat = sfmap.typeMap('np', 'SFfmt', self.data.dtype)
                else:
                    logger.error('Missing dataFormat for object %s', self.objectName)
                    return

        if not hasattr(self, 'descr'):
            self.descr = b''

        for attr in ('level', 'status', 'errcode'):
            if not hasattr(self, attr):
                setattr(self, attr, 0)
