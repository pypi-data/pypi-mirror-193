"""The definition of an SCOS-2000 table schema

Based on EGOS-MCS-S2K-ICD-0001 issue 7.2-FINAL (2019-12-13)
"""
import io
import string
from pathlib import Path
from zipfile import ZipFile

from .instance import Table, TableCell
from .checker import SCOSTableChecker, ALL_CHECKERS
from .reporter import StdErrReporter
from .schema import (
    TableDefinition, ColumnDefinition,
    Number, Boolean, String, ParameterNature,
    CalibrationCategoryColumn, EventPacketIndicator,
    EndianessColumn, OutputViewColumn, InterpolationColumn,
    ParameterNatureColumn, JustifyColumn, NumericFormatTypeColumn,
    RadixColumn, LimitInterpretationColumn, LimitTypeInterpretationColumn,
    MonitoringCheckFlagColumn, PacketHeaderElementTypeColumn, PlannableColumn,
    CommandVerificationColumn, CommandInputFormatColumn, CommandCategoryColumn,
    CommandInterlockColumn, DisplayFormatColumn, IntegerFormatTypeColumn,
    )
from .parametertypes import ParameterType, SignedIntegerParameter, UnsignedIntegerParameter
from .synthetic import DynamicSyntheticParameter


class SyntheticImplementationMissingError(RuntimeError):
    """Raised when the implementation of a synthetic parameter is missing"""


class VDFTable(TableDefinition):
    """The vdf.dat table in SCOS

    Database meta and version information"""
    def __init__(self):
        super().__init__('vdf', [
            ColumnDefinition('VDF_NAME', String(8), optional=False),
            ColumnDefinition('VDF_COMMENT', String(32), optional=True),
            ColumnDefinition('VDF_DOMAIN', Number(5), optional=True),
            ColumnDefinition('VDF_RELEASE', Number(5), optional=True, default='0'),
            ColumnDefinition('VDF_ISSUE', Number(5), optional=True, default='0'),
            ])


class PCFTable(TableDefinition):
    """The pcf.dat table in SCOS

    Monitoring parameters characteristics"""
    def __init__(self):
        super().__init__('pcf', [
            ColumnDefinition('PCF_NAME', String(8), optional=False, is_key=True),
            ColumnDefinition('PCF_DESCR', String(24), optional=True),
            ColumnDefinition('PCF_PID', Number(10), optional=True),
            ColumnDefinition('PCF_UNIT', String(4), optional=True),
            ColumnDefinition('PCF_PTC', Number(2), optional=False),
            ColumnDefinition('PCF_PFC', Number(5), optional=False),
            ColumnDefinition('PCF_WIDTH', Number(6), optional=True),
            ColumnDefinition('PCF_VALID', String(8), optional=True),
            ColumnDefinition('PCF_RELATED', String(8), optional=True),
            ColumnDefinition('PCF_CATEG', CalibrationCategoryColumn(), optional=False),
            ColumnDefinition('PCF_NATUR', ParameterNatureColumn(), optional=False),
            ColumnDefinition('PCF_CURTX', String(10), optional=True),
            ColumnDefinition('PCF_INTER', InterpolationColumn(), optional=True, default='F'),
            ColumnDefinition('PCF_USCON', Boolean(), optional=True, default='N'),
            ColumnDefinition('PCF_DECIM', Number(3), optional=True),
            ColumnDefinition('PCF_PARVAL', String(14), optional=True),
            ColumnDefinition('PCF_SUBSYS', String(8), optional=True),
            ColumnDefinition('PCF_VALPAR', Number(5), optional=True, default='1'),
            ColumnDefinition('PCF_SPTYPE', OutputViewColumn(), optional=True),
            ColumnDefinition('PCF_CORR', Boolean(), optional=True, default='Y'),
            ColumnDefinition('PCF_OBTID', Number(5), optional=True),
            ColumnDefinition('PCF_DARC', Boolean('1', '0'), optional=True, default='0'),
            ColumnDefinition('PCF_ENDIAN', EndianessColumn(), optional=True, default='B'),
            ColumnDefinition('PCF_DESCR2', String(256), optional=True, default=''),
            ])

    def is_synthetic(self, value):
        """Whether or not ``value`` (of type ``ParameterNature``) is synthetic"""
        return value in [ParameterNature.SYNTHETIC,
                         ParameterNature.DYNAMIC,
                         ParameterNature.HARDCODED,
                         ParameterNature.SAVEDSYNTHETIC]


class PIDTable(TableDefinition):
    """The pid.dat table in SCOS

    Packet identification"""
    def __init__(self):
        super().__init__('pid', [
            ColumnDefinition('PID_TYPE', Number(3), optional=False, is_key=True),
            ColumnDefinition('PID_STYPE', Number(3), optional=False, is_key=True),
            ColumnDefinition('PID_APID', Number(5), optional=False, is_key=True),
            ColumnDefinition('PID_PI1_VAL', Number(10), optional=True, default='0', is_key=True),
            ColumnDefinition('PID_PI2_VAL', Number(10), optional=True, default='0', is_key=True),
            ColumnDefinition('PID_SPID', Number(10), optional=False, is_key=True),
            ColumnDefinition('PID_DESCR', String(64), optional=True),
            ColumnDefinition('PID_UNIT', String(8), optional=True),
            ColumnDefinition('PID_TPSD', Number(10), optional=True, default='-1'),
            ColumnDefinition('PID_DFHSIZE', Number(2), optional=False),
            ColumnDefinition('PID_TIME', Boolean(), optional=True, default='N'),
            ColumnDefinition('PID_INTER', Number(10), optional=True),
            ColumnDefinition('PID_VALID', Boolean(), optional=True, default='Y'),
            ColumnDefinition('PID_CHECK', Number(1), optional=True, default='0'),
            ColumnDefinition('PID_EVENT', EventPacketIndicator(), optional=True, default='N'),
            ColumnDefinition('PID_EVID', String(17), optional=True),
            ])


class PICTable(TableDefinition):
    """The pic.dat table in SCOS

    Packet identification criteria"""
    NONE_APID = 99999

    def __init__(self):
        super().__init__('pic', [
            ColumnDefinition('PIC_TYPE', Number(3), optional=False, is_key=True),
            ColumnDefinition('PIC_STYPE', Number(3), optional=False, is_key=True),
            ColumnDefinition('PIC_PI1_OFF', Number(5), optional=False),
            ColumnDefinition('PIC_PI1_WID', Number(3), optional=False),
            ColumnDefinition('PIC_PI2_OFF', Number(5), optional=False),
            ColumnDefinition('PIC_PI2_WID', Number(3), optional=False),
            ColumnDefinition('PIC_APID', Number(5), optional=True, is_key=True,
                             default=str(PICTable.NONE_APID)),
            ])


class TPCFTable(TableDefinition):
    """The tpcf.dat table in SCOS

    Telemetry packets characteristics"""
    def __init__(self):
        super().__init__('tpcf', [
            ColumnDefinition('TPCF_SPID', Number(10), optional=False, is_key=True),
            ColumnDefinition('TPCF_NAME', String(12), optional=True),
            ColumnDefinition('TPCF_SIZE', Number(8), optional=True),
            ])


class PLFTable(TableDefinition):
    """The plf.dat table in SCOS

    Parameter location in fixed packets"""
    def __init__(self):
        super().__init__('plf', [
            ColumnDefinition('PLF_NAME', String(8), optional=False, is_key=True),
            ColumnDefinition('PLF_SPID', Number(10), optional=False, is_key=True),
            ColumnDefinition('PLF_OFFBY', Number(5), optional=False),
            ColumnDefinition('PLF_OFFBI', Number(1), optional=False),
            ColumnDefinition('PLF_NBOCC', Number(4), optional=True, default='1'),
            ColumnDefinition('PLF_LGOCC', Number(5), optional=True, default='0'),
            ColumnDefinition('PLF_TIME', Number(9), optional=True, default='0'),
            ColumnDefinition('PLF_TDOCC', Number(9), optional=True, default='1'),
            ])


class CURTable(TableDefinition):
    """The cur.dat table in SCOS

    Calibration conditional selection"""
    def __init__(self):
        super().__init__('cur', [
            ColumnDefinition('CUR_PNAME', String(8), optional=False, is_key=True),
            ColumnDefinition('CUR_POS', Number(2), optional=False, is_key=True),
            ColumnDefinition('CUR_RLCHK', String(8), optional=False),
            ColumnDefinition('CUR_VALPAR', Number(5), optional=False),
            ColumnDefinition('CUR_SELECT', String(10), optional=False),
            ])


class CAFTable(TableDefinition):
    """The caf.dat table in SCOS

    Numerical calibrations"""
    def __init__(self):
        super().__init__('caf', [
            ColumnDefinition('CAF_NUMBR', String(10), optional=False, is_key=True),
            ColumnDefinition('CAF_DESCR', String(32), optional=True),
            ColumnDefinition('CAF_ENGFMT', NumericFormatTypeColumn(), optional=False),
            ColumnDefinition('CAF_RAWFMT', NumericFormatTypeColumn(), optional=False),
            ColumnDefinition('CAF_RADIX', RadixColumn(), optional=True),
            ColumnDefinition('CAF_UNIT', String(4), optional=True),
            ColumnDefinition('CAF_NCURVE', Number(3), optional=True),
            ColumnDefinition('CAF_INTER', InterpolationColumn(), optional=True, default='F'),
            ])


class CAPTable(TableDefinition):
    """The cap.dat table in SCOS

    Numerical calibration definitions"""
    def __init__(self):
        super().__init__('cap', [
            ColumnDefinition('CAP_NUMBR', String(10), optional=False, is_key=True),
            ColumnDefinition('CAP_XVALS', String(14), optional=False, is_key=True),
            ColumnDefinition('CAP_YVALS', String(14), optional=False),
            ])


class TXFTable(TableDefinition):
    """The txf.dat table in SCOS

    Textual calibrations"""
    def __init__(self):
        super().__init__('txf', [
            ColumnDefinition('TXF_NUMBR', String(10), optional=False, is_key=True),
            ColumnDefinition('TXF_DESCR', String(32), optional=True),
            ColumnDefinition('TXF_RAWFMT', NumericFormatTypeColumn(), optional=False),
            ColumnDefinition('TXF_NALIAS', Number(3), optional=True),
            ])


class TXPTable(TableDefinition):
    """The txp.dat table in SCOS

    Textual calibrations definition"""
    def __init__(self):
        super().__init__('txp', [
            ColumnDefinition('TXP_NUMBR', String(10), optional=False, is_key=True),
            ColumnDefinition('TXP_FROM', String(14), optional=False, is_key=True),
            ColumnDefinition('TXP_TO', String(14), optional=False),
            ColumnDefinition('TXP_ALTXT', String(14), optional=False),
            ])


class MCFTable(TableDefinition):
    """The mcf.dat table in SCOS

    Polynomial calibrations definitions"""
    def __init__(self):
        super().__init__('mcf', [
            ColumnDefinition('MCF_IDENT', String(10), optional=False, is_key=True),
            ColumnDefinition('MCF_DESCR', String(32), optional=True),
            ColumnDefinition('MCF_POL1', String(14), optional=False),
            ColumnDefinition('MCF_POL2', String(14), optional=True, default='0'),
            ColumnDefinition('MCF_POL3', String(14), optional=True, default='0'),
            ColumnDefinition('MCF_POL4', String(14), optional=True, default='0'),
            ColumnDefinition('MCF_POL5', String(14), optional=True, default='0'),
            ])


class LGFTable(TableDefinition):
    """The lgf.dat table in SCOS

    Logarithmic calibrations definitions"""
    def __init__(self):
        super().__init__('lgf', [
            ColumnDefinition('LGF_IDENT', String(10), optional=False, is_key=True),
            ColumnDefinition('LGF_DESCR', String(32), optional=True),
            ColumnDefinition('LGF_POL1', String(14), optional=False),
            ColumnDefinition('LGF_POL2', String(14), optional=True, default='0'),
            ColumnDefinition('LGF_POL3', String(14), optional=True, default='0'),
            ColumnDefinition('LGF_POL4', String(14), optional=True, default='0'),
            ColumnDefinition('LGF_POL5', String(14), optional=True, default='0'),
            ])


class OCFTable(TableDefinition):
    """The ocf.dat table in SCOS

    Monitoring checks"""
    def __init__(self):
        super().__init__('ocf', [
            ColumnDefinition('OCF_NAME', String(8), optional=False, is_key=True),
            ColumnDefinition('OCF_NBCHCK', Number(2), optional=False),
            ColumnDefinition('OCF_NBOOL', Number(2), optional=False),
            ColumnDefinition('OCF_INTER', LimitInterpretationColumn(), optional=False),
            ColumnDefinition('OCF_CODIN', LimitTypeInterpretationColumn(), optional=False),
            ])


class OCPTable(TableDefinition):
    """the ocp.dat table in SCOS

    Monitoring checks definition"""
    def __init__(self):
        super().__init__('ocp', [
            ColumnDefinition('OCP_NAME', String(8), optional=False, is_key=True),
            ColumnDefinition('OCP_POS', Number(2), optional=False, is_key=True),
            ColumnDefinition('OCP_TYPE', MonitoringCheckFlagColumn(), optional=False),
            ColumnDefinition('OCP_LVALU', String(14), optional=True),
            ColumnDefinition('OCP_HVALU', String(14), optional=True),
            ColumnDefinition('OCP_RLCHK', String(8), optional=True),
            ColumnDefinition('OCP_VALPAR', Number(5), optional=True, default='1'),
            ])


class VPDTable(TableDefinition):
    """The vpd.dat table in SCOS

    Variable packet definition"""
    def __init__(self):
        super().__init__('vpd', [
            ColumnDefinition('VPD_TPSD', Number(10), optional=False, is_key=True),
            ColumnDefinition('VPD_POS', Number(4), optional=False, is_key=True),
            ColumnDefinition('VPD_NAME', String(8), optional=False),
            ColumnDefinition('VPD_GRPSIZE', Number(3), optional=True, default='0'),
            ColumnDefinition('VPD_FIXREP', Number(3), optional=True, default='0'),
            ColumnDefinition('VPD_CHOICE', Boolean(), optional=True, default='N'),
            ColumnDefinition('VPD_PIDREF', Boolean(), optional=True, default='N'),
            ColumnDefinition('VPD_DISDESC', String(16), optional=True),
            ColumnDefinition('VPD_WIDTH', Number(2), optional=False),
            ColumnDefinition('VPD_JUSTIFY', JustifyColumn(), optional=True, default='L'),
            ColumnDefinition('VPD_NEWLINE', Boolean(), optional=True, default='N'),
            ColumnDefinition('VPD_DCHAR', Number(1), optional=True, default='0'),
            ColumnDefinition('VPD_FORM', DisplayFormatColumn(), optional=True, default='N'),
            ColumnDefinition('VPD_OFFSET', Number(6), optional=True, default='0'),
            ])


class TCPTable(TableDefinition):
    """The tcp.dat table in SCOS

    TC packet header characteristics"""
    def __init__(self):
        super().__init__('tcp', [
            ColumnDefinition('TCP_ID', String(8), optional=False, is_key=True),
            ColumnDefinition('TCP_DESC', String(24), optional=True),
            ])


class PCPCTable(TableDefinition):
    """The pcpc.dat table in SCOS

    TC packet header parameters"""
    def __init__(self):
        super().__init__('pcpc', [
            ColumnDefinition('PCPC_PNAME', String(8), optional=False, is_key=True),
            ColumnDefinition('PCPC_DESC', String(24), optional=False),
            ColumnDefinition('PCPC_CODE', IntegerFormatTypeColumn(), optional=True, default='U'),
            ])


class PCDFTable(TableDefinition):
    """The pcdf.dat table in SCOS

    Packet heaer definitions"""
    def __init__(self):
        super().__init__('pcdf', [
            ColumnDefinition('PCDF_TCNAME', String(8), optional=False, is_key=True),
            ColumnDefinition('PCDF_DESC', String(24), optional=True),
            ColumnDefinition('PCDF_TYPE', PacketHeaderElementTypeColumn(), optional=False),
            ColumnDefinition('PCDF_LEN', Number(4), optional=False),
            ColumnDefinition('PCDF_BIT', Number(4), optional=False, is_key=True),
            ColumnDefinition('PCDF_PNAME', String(8), optional=True),
            ColumnDefinition('PCDF_VALUE', String(10), optional=False),
            ColumnDefinition('PCDF_RADIX', RadixColumn(), optional=True, default='H'),
            ])


class CCFTable(TableDefinition):
    """The ccf.dat table in SCOS

    Command characteristics"""
    def __init__(self):
        super().__init__('ccf', [
            ColumnDefinition('CCF_CNAME', String(8), optional=False, is_key=True),
            ColumnDefinition('CCF_DESCR', String(24), optional=False),
            ColumnDefinition('CCF_DESCR2', String(64), optional=True),
            ColumnDefinition('CCF_CTYPE', String(8), optional=True),
            ColumnDefinition('CCF_CRITICAL', Boolean(), optional=True, default='N'),
            ColumnDefinition('CCF_PKTID', String(8), optional=False),
            ColumnDefinition('CCF_TYPE', Number(3), optional=True),
            ColumnDefinition('CCF_STYPE', Number(3), optional=True),
            ColumnDefinition('CCF_APID', Number(5), optional=True),
            ColumnDefinition('CCF_NPARS', Number(3), optional=True),
            ColumnDefinition('CCF_PLAN', PlannableColumn(), optional=True, default='N'),
            ColumnDefinition('CCF_EXEC', Boolean(), optional=True, default='Y'),
            ColumnDefinition('CCF_ILSCOPE', CommandInterlockColumn(), optional=True, default='N'),
            ColumnDefinition('CCF_ILSTAGE', CommandVerificationColumn(),
                             optional=True, default='C'),
            ColumnDefinition('CCF_SUBSYS', Number(3), optional=True),
            ColumnDefinition('CCF_HIPRI', Boolean(), optional=True, default='N'),
            ColumnDefinition('CCF_MAPID', Number(2), optional=True),
            ColumnDefinition('CCF_DEFSET', String(8), optional=True),
            ColumnDefinition('CCF_RAPID', Number(5), optional=True),
            ColumnDefinition('CCF_ACK', Number(2), optional=True),
            ColumnDefinition('CCF_SUBSCHEDID', Number(5), optional=True),
            ])


class DSTTable(TableDefinition):
    """The dst.dat table in SCOS

    Command routing"""
    def __init__(self):
        super().__init__('dst', [
            ColumnDefinition('DST_APID', Number(5), optional=False, is_key=True),
            ColumnDefinition('DST_ROUTE', String(30), optional=False),
            ])


class CPCTable(TableDefinition):
    """The cpc.dat table in SCOS

    Command parameters"""
    def __init__(self):
        super().__init__('cpc', [
            ColumnDefinition('CPC_NAME', String(8), optional=False, is_key=True),
            ColumnDefinition('CPC_DESCR', String(24), optional=True),
            ColumnDefinition('CPC_PTC', Number(2), optional=False),
            ColumnDefinition('CPC_PFC', Number(5), optional=False),
            ColumnDefinition('CPC_DISPFMT', CommandInputFormatColumn(),
                             optional=True, default='R'),
            ColumnDefinition('CPC_RADIX', RadixColumn(), optional=True, default='D'),
            ColumnDefinition('CPC_UNIT', String(4), optional=True),
            ColumnDefinition('CPC_CATEG', CommandCategoryColumn(), optional=True, default='N'),
            ColumnDefinition('CPC_PRFREF', String(10), optional=True),
            ColumnDefinition('CPC_CCAREF', String(10), optional=True),
            ColumnDefinition('CPC_PAFREF', String(10), optional=True),
            ColumnDefinition('CPC_INTER', OutputViewColumn(), optional=True, default='R'),
            ColumnDefinition('CPC_DEFVAL', String(17), optional=True),
            ColumnDefinition('CPC_CORR', Boolean(), optional=True, default='Y'),
            ColumnDefinition('CPC_OBTIP', Number(5), optional=True, default='0'),
            ColumnDefinition('CPC_DESCR2', String(256), optional=True, default=''),
            ColumnDefinition('CPC_ENDIAN', EndianessColumn(), optional=True, default='B'),
            ])


class PTVTable(TableDefinition):
    """The ptv.dat table in SCOS

    Commands pre-transmission validation"""
    def __init__(self):
        super().__init__('ptv', [
            ColumnDefinition('PTV_CNAME', String(8), optional=False, is_key=True),
            ColumnDefinition('PTV_PARNAM', String(8), optional=False, is_key=True),
            ColumnDefinition('PTV_INTER', OutputViewColumn(), optional=True, default='R'),
            ColumnDefinition('PTV_VAL', String(17), optional=False),
            ])


class SCOS:
    """An SCOS-2000 database instance

    This is your main entry point for the use of SCOS-2000 databases.

    To merge this SCOS-2000 database with another database (for example if
    you have an instrument’s database but also a separate database for the
    spacecraft), instatiate both databases and then merge them like this::

        instrument = SCOS('instrumentdb.zip')
        spacecraft = SCOS('spacecraftdb.zip')

        if spacecraft.can_merge(instrument):
            spacecraft.merge(instrument)

    It’s a good idea to run ``can_merge`` first to ensure there are no
    collisions in any of the tables.

    To verify the correctness of the database definition, you can run
    ``check``. It allows you to have a custom set of checkers and also
    a custom reporter, if you don’t want the errors to be written to stderr.

    You can access the various tables (and their rows) like this::

        scos = SCOS('db.zip')
        for row in scos.pcf.rows:
            # do something with each pcfdefinition from the pcf table

    Each table is a ``Table`` instance allowing convenient access to the
    rows with the ``rows`` property and even accessing specific rows by
    their primary key by calling ``.get(...)`` and the primary key values
    as a ``tuple``.

    Each row is a ``TableRow`` instance allowing convenient access to

    - the row’s definition with ``row.column`` (of type ``ColumnDefinition``)
    - the row’s fields by name (``row['PCF_NAME']``) or ``row.get()``
    - the row’s line number via ``row.linenr``
    - all row’s fields by iterating them (``for field in row: ...``)
    """

    class PCFNatureCell(TableCell):
        @property
        def is_synthetic(self):
            return self.table.definition.is_synthetic(self.value)

    class PCFTableInstance(Table):
        def create_cell(self, column, field):
            if column.name == 'PCF_NATUR':
                return SCOS.PCFNatureCell(self, column, field)
            return super().create_cell(column, field)

    def __init__(self, path):
        """Instantiate from the SCOS-2000 definition at ``path``.

        ``path`` may either be a folder with the ``.dat`` files or
        a ``.zip`` file containing the ``.dat`` files.
        """
        self.basepath = Path(path)

        self.ziparchive = None
        if self.basepath.is_file() and self.basepath.suffix == '.zip':
            self.ziparchive = ZipFile(self.basepath, 'r')

        self.tables = {
            'vdf': Table(self, VDFTable()).parse(),
            'pcf': SCOS.PCFTableInstance(self, PCFTable()).parse(),
            'cur': Table(self, CURTable()).parse(),
            'caf': Table(self, CAFTable()).parse(),
            'cap': Table(self, CAPTable()).parse().sort(True),
            'txf': Table(self, TXFTable()).parse(),
            'txp': Table(self, TXPTable()).parse().sort(True),
            'mcf': Table(self, MCFTable()).parse(),
            'lgf': Table(self, LGFTable()).parse(),
            'ocf': Table(self, OCFTable()).parse(),
            'ocp': Table(self, OCPTable()).parse(),
            'pid': Table(self, PIDTable()).parse(),
            'pic': Table(self, PICTable()).parse(),
            'tpcf': Table(self, TPCFTable()).parse(),
            'plf': Table(self, PLFTable()).parse(),
            'vpd': Table(self, VPDTable()).parse(),
            # TODO 'grp': Table(self, GRPTable()).parse(),
            # TODO 'grpa': Table(self, GRPATable()).parse(),
            # TODO 'grpk': Table(self, GRPKTable()).parse(),
            # TODO 'dpf': Table(self, DPFTable()).parse(),
            # TODO 'dpc': Table(self, DPCTable()).parse(),
            # TODO 'gpf': Table(self, GPFTable()).parse(),
            # TODO 'gpc': Table(self, GPCTable()).parse(),
            # TODO 'spf': Table(self, SPFTable()).parse(),
            # TODO 'spc': Table(self, SPCTable()).parse(),
            # TODO 'ppf': Table(self, PPFTable()).parse(),
            # TODO 'ppc': Table(self, PPCTable()).parse(),
            'tcp': Table(self, TCPTable()).parse(),
            'pcpc': Table(self, PCPCTable()).parse(),
            'pcdf': Table(self, PCDFTable()).parse(),
            'ccf': Table(self, CCFTable()).parse(),
            'dst': Table(self, DSTTable()).parse(),
            'cpc': Table(self, CPCTable()).parse(),
            # TODO 'cdf': Table(self, CDFTable()).parse(),
            'ptv': Table(self, PTVTable()).parse(),
            # TODO 'csf': Table(self, CSFTable()).parse(),
            # TODO 'css': Table(self, CSSTable()).parse(),
            # TODO 'csp': Table(self, CSPTable()).parse(),
            # TODO 'cvs': Table(self, CVSTable()).parse(),
            # TODO 'cve': Table(self, CVETable()).parse(),
            # TODO 'cvp': Table(self, CVPTable()).parse(),
            # TODO 'pst': Table(self, PSTTable()).parse(),
            # TODO 'psv': Table(self, PSVTable()).parse(),
            # TODO 'cps': Table(self, CPSTable()).parse(),
            # TODO 'pvs': Table(self, PVSTable()).parse(),
            # TODO 'psm': Table(self, PSMTable()).parse(),
            # TODO 'cca': Table(self, CCATable()).parse(),
            # TODO 'ccs': Table(self, CCSTable()).parse(),
            # TODO 'paf': Table(self, PAFTable()).parse(),
            # TODO 'pas': Table(self, PASTable()).parse(),
            # TODO 'prf': Table(self, PRFTable()).parse(),
            # TODO 'prv': Table(self, PRVTable()).parse(),
            }

        self.synthetics = {}
        """The ``synthetics`` dictionary contains the definitions for all
        synthetic parameters. The key is the parameter's name, the value an
        instance of ``SyntheticParameterDefinition``."""
        self.synthetics_in_spid = {}
        """A mapping of SPID to all synthetic parameters that can be evaluated
        in a packet with this SPID (because all input parameters are present in
        that packet according to the PLF table."""
        self.load_synthetics()
        self.parse_synthetics()

        if self.ziparchive is not None:
            self.ziparchive.close()

    def __getattr__(self, name):
        if name in self.tables:
            return self.tables[name]
        raise AttributeError()

    @property
    def version(self):
        """Return the version string of this SCOS2000 instance
        Specifically the VDF release and issue
        """
        return str(self.vdf.rows[0]['VDF_RELEASE'].value) \
             + "." \
             + str(self.vdf.rows[0]['VDF_ISSUE'].value)

    def check(self, checkers=None, reporter=None, pedantic=False):
        """Run all ``checkers`` on this database

        If ``checkers`` is left ``None``, all registered checkers will be run.

        If ``reporter`` is left ``None``, the ``StdErrReporter`` will be used.

        The ``pedantic`` flag can be used to make the checks extra annoying
        (they might check the range for values that are actually ignored in the
        given context).
        """
        if checkers is None:
            checkers = ALL_CHECKERS
        if reporter is None:
            reporter = StdErrReporter()
        for cls in checkers:
            checker = cls(self, reporter, pedantic)
            for table in self.tables.values():
                checker.visit(table)

    def can_merge(self, other):
        """Verify whether the ``other`` SCOS can be merged into this

        This function checks for duplicate/clashing definitions.
        """
        return all(t.can_merge(other.tables[n])
                   for n, t in self.tables.items()) \
               and \
               len(set(self.synthetics.keys()) & set(other.synthetics.keys())) == 0

    def merge(self, other):
        """Merge the SCOS ``other`` into this

        You should check ``can_merge`` before-hand to verify that a
        merge will not cause clashing definitions.
        """
        for name, table in self.tables.items():
            table.merge(other.tables[name])
        self.synthetics.update(other.synthetics)

    def load_synthetics(self):
        """Load all synthetic parameters"""
        self.synthetics = {}

        for row in self.pcf.rows:
            paramdef = None
            if row['PCF_NATUR'].value == ParameterNature.DYNAMIC:
                paramdef = DynamicSyntheticParameter(row)
            elif row['PCF_NATUR'].value == ParameterNature.HARDCODED:
                pass
            elif row['PCF_NATUR'].value == ParameterNature.SYNTHETIC:
                pass
            elif row['PCF_NATUR'].value == ParameterNature.SAVEDSYNTHETIC:
                pass
            else:
                # not a synthetic parameter
                continue

            if paramdef is None:
                raise NotImplementedError(f"PCF_NATUR = {row['PCF_NATUR'].value} "
                                          f"not supported for {row['PCF_NAME'].value}")
            self.synthetics[row['PCF_NAME'].value] = paramdef

    def parse_synthetics(self):
        """Parse and cache the synthetic parameter implementations"""
        for name, definition in self.synthetics.items():
            # find the definition file
            stream = self.open_textfile(name, path=self.basepath / 'synthetic')
            if stream is not None:
                definition.parse(stream)
            else:
                raise SyntheticImplementationMissingError("No implementation found "
                                                          f"for synthetic parameter {name}")

        # build a list of all SPIDs with the parameters that are grouped in them
        spids = {}
        for plf in self.plf.rows:
            spid = plf['PLF_SPID'].value
            if spid not in spids:
                spids[spid] = set()
            spids[spid].add(plf['PLF_NAME'].value)

        self.synthetics_in_spid = {}
        for spid, params in spids.items():
            for name, definition in self.synthetics.items():
                if definition.inputs.issubset(params):
                    if spid not in self.synthetics_in_spid:
                        self.synthetics_in_spid[spid] = set()
                    self.synthetics_in_spid[spid].add(name)

    def open_table(self, tablename):
        """Return a context manager for the file with the given table name

        May return ``None`` if the file for that table does not exist
        """
        tablefilename = tablename + '.dat'
        return self.open_textfile(tablefilename)

    def open_textfile(self, filename, path=None):
        """Return a context manager for reading text from the file with the given name

        May return ``None`` if the file does not exist."""
        if path is None:
            path = self.basepath
        if self.ziparchive is not None:
            fullpath = [fn
                        for fn in self.ziparchive.namelist()
                        if Path(fn).name == filename]
            if len(fullpath) == 0:
                return None
            return ZipArchiveTextReader(self.ziparchive, fullpath[0])

        filepath = path / filename
        if not filepath.is_file():
            return None
        return open(filepath, 'rt', encoding='utf-8', newline='')


class ZipArchiveTextReader:
    """Context manager for reading text files from an open zipfile"""
    def __init__(self, archive, path):
        self.archive = archive
        self.filepath = path
        self.filehandle = None
        self.textstream = None

    def __enter__(self):
        self.filehandle = self.archive.open(self.filepath, 'r')
        self.textstream = io.TextIOWrapper(self.filehandle, encoding='utf-8', newline='')
        return self.textstream

    def __exit__(self, *args, **kwargs):
        if self.textstream is not None:
            self.textstream.close()
        if self.filehandle is not None:
            self.filehandle.close()


class ExtraCAPDefinitions(SCOSTableChecker):
    """Report any CAP definitions that don't have a matching CAF entry"""
    ACCEPTED_TABLES = (CAPTable,)

    def check_row(self, row):
        if (row['CAP_NUMBR'].value,) not in self.scos.caf.index:
            self.error(f"CAP {row['CAP_NUMBR'].value} does "
                       "not have a matching CAF entry.")


class ExtraCAFEntries(SCOSTableChecker):
    """Report any CAF entry that has not the exact right amount of CAP rows"""
    ACCEPTED_TABLES = (CAFTable,)

    def check_row(self, row):
        rows = [r for r in self.scos.cap.rows
                if r['CAP_NUMBR'].value == row['CAF_NUMBR'].value]
        expected = row['CAF_NCURVE'].value
        if len(rows) != expected:
            self.error(f"{row['CAF_NUMBR'].value} should have {expected} CAP entries "
                       f"but has {len(rows)}")


class ExtraCalibrationDefinitions(SCOSTableChecker):
    """Report any unused CAF, TXF, MCF definitions"""
    ACCEPTED_TABLES = (CAFTable, TXFTable, MCFTable)

    def check_row(self, row):
        used = any(r['PCF_CURTX'] == row[0]
                   for r in self.scos.pcf.rows)
        if not used:
            self.error(f"{row[0].value} is not used")


class FieldLengthChecks(SCOSTableChecker):
    """Check that the fields are not longer than accepted by the definition"""

    def check_row(self, row):
        for colidx, cell in enumerate(row):
            rawlen = len(cell.rawvalue)
            coltype = cell.column.type
            allowed = -1

            if isinstance(coltype, String):
                allowed = coltype.maxlen
            elif isinstance(coltype, Number):
                allowed = coltype.digits
            elif isinstance(coltype, Boolean):
                allowed = max(len(coltype.true), len(coltype.false))

            if -1 < allowed < rawlen:
                self.error(f"Cell {colidx+1} ('{cell.rawvalue}') is too long: "
                           f"{rawlen}, max length: {allowed}")

    def accept(self, _):
        return True


class ValidityStateDefinitionChecker(SCOSTableChecker):
    """Check that TM parameters with validity parameters set are okay

    I.e. checking that they have a check value set and that the validy
    parameter type is actually of some integer type.
    """
    ACCEPTED_TABLES = (PCFTable,)

    def check_row(self, row):
        # TODO: check for circular state validation
        # TODO: synthetic parameters may be used for state validation
        validparamname = row['PCF_VALID'].value
        if validparamname is None:
            return
        validparamdef = [other for other in row.table.rows
                         if other['PCF_NAME'] == validparamname]

        if len(validparamdef) == 0:
            self.error(f"{row['PCF_NAME']} uses non-existing {validparamname} as "
                        "state validity parameter.")
            return
        validparamdef = validparamdef[0]

        ptype = ParameterType.resolve(validparamdef)
        if not isinstance(ptype, (SignedIntegerParameter, UnsignedIntegerParameter)):
            self.error(f"{validparamname} is used as a state validity parameter "
                       f"for {row['PCF_NAME']}, but is not signed or unsigned int")
            return


class OnlyAllowedCharactersChecker(SCOSTableChecker):
    """Check that forbidden characters are not used in CHAR columns part of the key"""

    ALLOWED = string.ascii_letters + string.digits + '_+-. '

    def check_row(self, row):
        for colidx, cell in enumerate(row):
            if not isinstance(cell.column.type, String) or not cell.column.is_key:
                continue

            if any(letter not in self.ALLOWED for letter in cell.rawvalue):
                self.error(f"Cell {colidx+1} contains at least one character "
                            "that is not allowed.")
                continue

    def accept(self, _):
        return True


class StaticMonitorValueChecker(SCOSTableChecker):
    """Verify that monitor parameters of nature 'constant' have a PARVAL set"""
    ACCEPTED_TABLES = (PCFTable,)

    def check_row(self, row):
        if row['PCF_NATUR'] != ParameterNature.CONSTANT:
            return

        rawvalue = row['PCF_PARVAL'].rawvalue

        if rawvalue is None or len(rawvalue) == 0:
            self.error(f"PARVAL 'None' (cell 16) not allowed for "
                       f"{row['PCF_NAME']}, because PCF_NATUR is 'C' (constant).")


class BitOffsetChecker(SCOSTableChecker):
    """Verify that bit-offset values are only in the range 0..7"""
    ACCEPTED_TABLES = (PLFTable,)

    def check_row(self, row):
        if not (0 <= int(row['PLF_OFFBI'].value) <= 7):
            self.error(f"{row['PLF_NAME']}: PLF_OFFBI outside 0..7")


class PLFTimeDelayChecker(SCOSTableChecker):
    """Verify that the time delay parameter is in a valid range"""
    ACCEPTED_TABLES = (PLFTable,)

    def check_row(self, row):
        if row['PLF_NBOCC'].value == 1 and not self.pedantic:
            return
        tdocc = row['PLF_TDOCC'].value
        if not (0 < tdocc <= 4080000):
            self.error(f"Invalid TDOCC parameter value {tdocc}")
