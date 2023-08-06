"""SCOS table schema definition"""
import enum


class IndicatorType(enum.Enum):
    """Event indicator types"""
    UNKNOWN = None
    """Undefined"""

    NOEVENT = 'N'
    """No event should be triggered"""

    INFO = 'I'
    """An event of 'info' severity should be triggered"""

    WARNING = 'W'
    """An event of 'warning' severity should be triggered"""

    ALARM = 'A'
    """An event of 'alarm' severity should be triggered"""


class CalibrationCategory(enum.Enum):
    NUMERICAL = 'N'
    STATUS = 'S'
    TEXT = 'T'


class ParameterNature(enum.Enum):
    RAW = 'R'
    DYNAMIC = 'D'
    SYNTHETIC = 'P'
    HARDCODED = 'H'
    SAVEDSYNTHETIC = 'S'
    CONSTANT = 'C'


class InterpolationBehaviour(enum.Enum):
    UNDEFINED = None
    EXTRAPOLATE = 'P'
    INVALID = 'F'


class OutputView(enum.Enum):
    ENGINEERING = 'E'
    RAW = 'R'


class Endianess(enum.Enum):
    BIG_ENDIAN = 'B'
    LITTLE_ENDIAN = 'L'


class Justification(enum.Enum):
    LEFT = 'L'
    RIGHT = 'R'
    CENTER = 'C'


class IntegerFormatType(enum.Enum):
    SIGNEDINT = 'I'
    UNSIGNEDINT = 'U'


class NumericFormatType(enum.Enum):
    SIGNEDINT = 'I'
    UNSIGNEDINT = 'U'
    REAL = 'R'

    def convert(self, text):
        """Convert the given text into this format's type

        E.g. if ``self == NumericFormatType.REAL`` convert will return a ``float``
        """
        if self == NumericFormatType.REAL:
            return float(text)
        if self in [NumericFormatType.SIGNEDINT, NumericFormatType.UNSIGNEDINT]:
            return int(text)
        return ValueError()


class Radix(enum.Enum):
    """The radix of an unsigned integer value's text representation"""
    UNDEFINED = None
    DECIMAL = 'D'
    HEXADECIMAL = 'H'
    OCTAL = 'O'

    def convert(self, text):
        """Convert the given text to an unsigned int given this radix"""
        if self == Radix.DECIMAL:
            return int(text)
        if self == Radix.HEXADECIMAL:
            return int(text, 16)
        if self == Radix.OCTAL:
            return int(text, 0)
        raise ValueError(f"Cannot interprete {text} with radix {self}")


class LimitInterpretation(enum.Enum):
    """What value to use to interprete limit values"""

    UNCALIBRATED = 'U'
    """Use RAW values"""
    CALIBRATED = 'C'
    """Use ENG values"""


class LimitTypeInterpretation(enum.Enum):
    """What type the value is that is used to interprete limit values"""

    REAL = 'R'
    """Floating point"""

    TEXT = 'A'
    """ASCII text"""

    INTEGER = 'I'
    """Signed or unsigned integer values"""


class MonitoringCheckFlag(enum.Enum):
    """Of what type a monitoring check is"""

    SOFT_LIMIT = 'S'
    HARD_LIMIT = 'H'
    DELTA = 'D'
    CONSISTENCY = 'C'
    EVENT_ONLY = 'E'


class PacketHeaderElementType(enum.Enum):
    FIXED = 'F'
    APID = 'A'
    SERVICETYPE = 'T'
    SERVICESUBTYPE = 'S'
    ACK = 'K'
    OTHER = 'P'


class Plannable(enum.Enum):
    ALL = 'A'
    FLIGHTDYNAMICS = 'F'
    SOC = 'S'
    NOT = 'N'


class CommandInterlock(enum.Enum):
    GLOBAL = 'G'
    LOCAL = 'L'
    SUBSYSTEM = 'S'
    BELONG = 'B'
    NONE = 'N'


class CommandVerification(enum.Enum):
    RECEPTION = 'R'
    ACCEPTANCE = 'R'
    UPLINK = 'U'
    ONBOARDRECEPTION = 'O'
    ONBOARDACCEPTANCE = 'O'
    APPACCEPTANCE = 'A'
    COMPLETION = 'C'


class CommandInputFormat(enum.Enum):
    ASCII = 'A'
    SIGNEDINT = 'I'
    UNSIGNEDINT = 'U'
    REAL = 'R'
    ABSTIME = 'T'
    RELTIME = 'D'


class CommandCategory(enum.Enum):
    NUMERIC = 'C'
    TEXTUAL = 'T'
    BOTH = 'B'
    COMMANDID = 'A'
    PARAMETERID = 'P'
    NONE = 'N'


class DisplayFormat(enum.Enum):
    BINARY = 'B'
    OCTAL = 'O'
    DECIMAL = 'D'
    HEXADECIMAL = 'H'
    NORMAL = 'N'


class TableColumnType:
    """The type of a column in an SCOS table definition"""

    def parse(self, text):
        """Parse the raw ``text`` and return the converted value"""
        if text is None:
            return None
        return self.do_parse(text)

    def do_parse(self, text):
        """Delegated parsing of the raw `text`"""
        raise NotImplementedError()


class Number(TableColumnType):
    """A numeric SCOS table column type"""
    def __init__(self, digits):
        super().__init__()
        self.digits = digits

    def do_parse(self, text):
        if text.startswith('0x'):
            return int(text[2:], 16)
        if text.startswith('0') and len(text) > 1:
            return int(text[1:], 8)
        if '.' in text or 'e' in text.lower():
            return float(text)
        return int(text)


class Boolean(TableColumnType):
    """A boolean SCOS table column type"""
    def __init__(self, true='Y', false='N'):
        super().__init__()
        self.true = true
        self.false = false

    def do_parse(self, text):
        return text == self.true


class String(TableColumnType):
    """A string of characters SCOS table column type"""
    def __init__(self, maxlen):
        super().__init__()
        self.maxlen = maxlen

    def do_parse(self, text):
        return text


class EnumColumnType(TableColumnType):
    """Generic definition of a column mapping to an enum type"""
    ENUM = None
    def do_parse(self, text):
        assert self.ENUM is not None
        return self.ENUM(text)


class EventPacketIndicator(EnumColumnType):
    """Behaviour description type for SCOS table columns"""
    ENUM = IndicatorType


class CalibrationCategoryColumn(EnumColumnType):
    """Calibration category type for SCOS table columns"""
    ENUM = CalibrationCategory


class ParameterNatureColumn(EnumColumnType):
    """Nature of a parameter as type for SCOS table columns"""
    ENUM = ParameterNature


class InterpolationColumn(EnumColumnType):
    """Interpolation behaviour definition for SCOS table columns"""
    ENUM = InterpolationBehaviour


class OutputViewColumn(EnumColumnType):
    """Parameter output view SCOS table column"""
    ENUM = OutputView


class EndianessColumn(EnumColumnType):
    """Endianess definition for an SCOS column"""
    ENUM = Endianess


class JustifyColumn(EnumColumnType):
    """Justification definition in ``vpd.dat``"""
    ENUM = Justification


class IntegerFormatTypeColumn(EnumColumnType):
    """Column identifying an integer format type"""
    ENUM = IntegerFormatType


class NumericFormatTypeColumn(EnumColumnType):
    """Column identifying a format type"""
    ENUM = NumericFormatType


class RadixColumn(EnumColumnType):
    """Column specifying the radix for unsigned integer display"""
    ENUM = Radix


class LimitInterpretationColumn(EnumColumnType):
    """Column with the flag for limit value interpretation"""
    ENUM = LimitInterpretation


class LimitTypeInterpretationColumn(EnumColumnType):
    """Column with the type for limit value interpretation"""
    ENUM = LimitTypeInterpretation


class MonitoringCheckFlagColumn(EnumColumnType):
    """Column for the type of monitoring checks"""
    ENUM = MonitoringCheckFlag


class PacketHeaderElementTypeColumn(EnumColumnType):
    """Column with packet header element type for PCDF table"""
    ENUM = PacketHeaderElementType


class PlannableColumn(EnumColumnType):
    """Column with Plannable type for command characteristics"""
    ENUM = Plannable


class CommandInterlockColumn(EnumColumnType):
    """Column with command interlock behaviour"""
    ENUM = CommandInterlock


class CommandVerificationColumn(EnumColumnType):
    """Column for the command verification type"""
    ENUM = CommandVerification


class CommandInputFormatColumn(EnumColumnType):
    """Column for CommandInputFormat in the command paramater table"""
    ENUM = CommandInputFormat


class CommandCategoryColumn(EnumColumnType):
    """Column for command category"""
    ENUM = CommandCategory


class DisplayFormatColumn(EnumColumnType):
    """Column for Display Format settings"""
    ENUM = DisplayFormat


class ColumnDefinition:
    """A column in an SCOS table definition"""
    def __init__(self,
                 name,
                 type_,
                 description="",
                 optional=False,
                 default=None,
                 is_key=False):
        self.name = name
        self.type = type_
        self.description = description
        self.optional = optional
        self.default = default
        self.is_key = is_key


class TableDefinition:
    """A generic definition of an SCOS table"""
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.primary_key = [cidx
                            for cidx, column in enumerate(self.columns)
                            if column.is_key]
        self.columnnames = [c.name for c in self.columns]
        self.filename = self.name + '.dat'

    @property
    def has_primary_key(self):
        """Whether or not a primary key is defined"""
        return len(self.primary_key) > 0
