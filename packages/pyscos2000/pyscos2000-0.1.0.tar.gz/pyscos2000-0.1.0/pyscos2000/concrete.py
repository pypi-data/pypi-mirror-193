"""Concrete parameter instances

Convenience classes for handling concrete instances of
telemetry parameters.
"""
import math
from collections import namedtuple

from .parametertypes import (
    ParameterType, SignedIntegerParameter, UnsignedIntegerParameter,
    FloatParameter,
)
from .schema import CalibrationCategory, InterpolationBehaviour, NumericFormatType


class PacketInterface:
    """Abstract packet interface

    When implementing a packet (e.g. PUS packet class) it must satisfy
    this interface to be able to use the SCOS wrapper
    """
    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return self.has(item)

    def get(self, item):
        """Get the parameter ``item``

        ``item`` can be one of these:
        - a number, referring to the position of the parameter in the payload
          of the packet
        - a string, identifying the parameter by name (8 character ``PCF_NAME``)

        If obtaining a parameter by name and there are multiple,
        only the first one is returned.

        Raises ``KeyError`` if the parameter is not there.
        """
        raise NotImplementedError("Must be implemented in a subclass")

    def get_all(self, name):
        """Get all parameters with the identifier ``name``

        Will always return a list, but it might be empty.
        """
        raise NotImplementedError("Must be implemented in a subclass")

    def has(self, item):
        """Whether or not parameter ``item`` is present

        ``item`` can be either a number to select the parameter by position or
        the 8-character parameter identifier.
        """
        raise NotImplementedError("Must be implemented in a subclass")

    def __len__(self):
        """The number of parameters in this packet"""
        raise NotImplementedError("Must be implemented in a subclass")

    def __iter__(self):
        yield from self.iter()

    def iter(self):
        """Iterate through the list of parameters"""
        raise NotImplementedError("Must be implemented in a subclass")


class Parameter:
    """A parameter with its actual values"""
    def __init__(self, packet, pcf):
        self.packet = packet
        self.pcf = pcf
        self.paramtype = ParameterType.resolve(self.pcf)
        self.unit = self.pcf['PCF_UNIT'].value or ''
        self._validity = None
        self._eng_value = None

    def get_hex(self):
        """Return the hex representation of this parameter"""
        raise NotImplementedError()

    def get_raw(self):
        """Return the raw value of this parameter

        The return value must be of the correct `ParameterType`
        """
        raise NotImplementedError()

    def get_eng(self):
        """Return the engineering value of this parameter"""
        if self._eng_value is None:
            self._eng_value = self.calibrate()
        return self._eng_value

    def calibrate(self):
        """Return the calibrated value from the raw value of this parameter"""
        # TODO #4 - evaluate conditional calibration
        calibcat = self.pcf['PCF_CATEG'].value
        calibparamname = self.pcf['PCF_CURTX'].value
        interpolation = self.pcf['PCF_INTER'].value  # TODO - use this!
        if calibparamname is None:
            return str(self.raw)

        calibparam = None
        if calibcat == CalibrationCategory.NUMERICAL:
            # no clear indication, we have to try which calibration is defined

            calibparam = self.scos.mcf.get(calibparamname)
            if calibparam is not None:
                # it is polynomial
                coeff = [float(v.value) for v in calibparam.items[2:]]
                return coeff[0] \
                     + coeff[1]*self.raw \
                     + coeff[2]*(self.raw**2) \
                     + coeff[3]*(self.raw**3) \
                     + coeff[4]*(self.raw**4)

            calibparam = self.scos.lgf.get(calibparamname)
            if calibparam is not None:
                # it is logarithmic
                coeff = [float(v.value) for v in calibparam.items[2:]]
                ln = math.log(self.raw)
                return 1.0/(coeff[0] +
                            coeff[1]*ln +
                            coeff[2]*(ln**2) +
                            coeff[3]*(ln**3) +
                            coeff[4]*(ln**4))

            calibdef = self.scos.caf.get(calibparamname)
            if calibdef is not None:
                # table-based numerical calibration
                return self.calibrate_cafcap(calibdef)

        elif calibcat == CalibrationCategory.STATUS:
            calibparam = self.scos.txf.get(calibparamname)
            rawformat = calibparam['TXF_RAWFMT'].value
            for txp in self.scos.txp.rows:
                if txp['TXP_NUMBR'].value != calibparam['TXF_NUMBR']:
                    continue
                range_from = rawformat.convert(txp['TXP_FROM'].value)
                range_to = rawformat.convert(txp['TXP_TO'].value)
                if range_from <= self.raw <= range_to:
                    return txp['TXP_ALTXT'].value

        elif calibcat == CalibrationCategory.TEXT:
            pass  # TODO #5

        else:
            raise NotImplementedError("Unknown, probably new, calibration "
                                      f"category {calibcat}")

        raise RuntimeError(f"Could not calibrate {self.name} (0x{self.hex}) "
                           f"with {calibparamname}")

    def calibrate_cafcap(self, cafdef):
        """Calibrate the parameter value using the CAF/CAP table"""
        interpolation = cafdef['CAF_INTER'].value
        values = interprete_cap(cafdef)
        lower = values[0]
        upper = values[-1]
        rawvalue = self.raw

        result = None

        # handle invalid extrapolations
        if interpolation == InterpolationBehaviour.INVALID and \
           (rawvalue < lower.x or rawvalue > upper.x):
            return result

        if rawvalue < lower.x:
            factor = (values[1].y - values[0].y)/float(values[1].x - values[0].x)
            result = factor*(rawvalue - values[0].x)
        elif rawvalue > upper.x:
            factor = (values[-2].y - values[-1].y)/float(values[-2].x - values[-1].x)
            result = upper.y + factor*(rawvalue - upper.x)
        else:
            # find the first value that's equal or bigger than rawvalue
            upperidx = 0
            while upperidx < len(values) and \
                  values[upperidx].x < rawvalue:
                upperidx += 1
            lower = values[upperidx-1]
            upper = values[upperidx]

            if rawvalue == lower.x:
                result = lower.y
            elif rawvalue == upper.x:
                result = upper.y
            else:
                factor = (upper.y - lower.y)/float(upper.x - lower.x)
                result = lower.y + factor*(rawvalue - lower.x)

        engfmt = cafdef['CAF_ENGFMT'].value
        if engfmt in (NumericFormatType.SIGNEDINT, NumericFormatType.UNSIGNEDINT):
            return int(result)
        if engfmt == NumericFormatType.REAL:
            return float(result)
        raise TypeError(engfmt)

    @property
    def hex(self):
        """Convenience accessor to ``get_hex``"""
        return self.get_hex()

    @property
    def raw(self):
        """Convenience accessor to ``get_raw``"""
        return self.get_raw()

    @property
    def eng(self):
        """Convenience accessor to ``get_eng``"""
        return self.get_eng()

    @property
    def scos(self):
        """Convenient quick access to the SCOS instance"""
        return self.pcf.scos

    @property
    def name(self):
        """The unique identifier of the parameter"""
        return self.pcf['PCF_NAME'].value

    @property
    def description(self):
        """The description of the parameter"""
        return self.pcf['PCF_DESCR'].value

    @property
    def is_valid(self):
        """Whether or not this parameter is valid"""
        if self._validity is None:
            self._validity = self.calculate_validity()
        return self._validity

    def for_humans(self):
        """Return the human readable version of the parameter

        This will return a tuple of ``(value, unit)``

        ``unit`` may be an empty string if no unit is given or required.

        ``value`` will be the engineering value formatted to the specifications.
        """
        eng = self.eng
        if isinstance(eng, float):
            eng = round(eng, self.pcf['PCF_DECIM'].value)
        return (eng, self.unit)

    def calculate_validity(self):
        """Calculate whether or not this parameter is valid"""
        validparam = self.pcf['PCF_VALID'].value
        if validparam is None:
            return True
        validvalue = self.pcf['PCF_VALPAR'].value

        validparamdef = self.scos.pcf.get(validparam)
        assert validparamdef is not None

        param = None
        if validparamdef['PCF_NATUR'].is_synthetic:
            synthparam = self.scos.synthetics.get(validparam, None)
            if synthparam is None:
                return False
            param = synthparam.evaluate(self.packet)

        if self.packet.has(validparam):
            param = self.packet.get(validparam)

        return param is not None \
           and param.is_valid \
           and param.raw == validvalue

    def __repr__(self):
        return f'<{self.name}: {self.hex}>'

    def __str__(self):
        return self.name


def interprete_cap(caf):
    """Interprete all CAP rows of this CAF table and return the x,y tuple as actual values

    The CAP /Y (raw/eng) values are stored as strings any must be interpreted
    using the CAF_RAWFMT, CAF_RADIX, and CAF_ENGFMT columns. This function
    takes care of it and returns a list of (x, y) tuples (Point instances)
    as their respective python types.
    """
    Point = namedtuple('Point', ('x', 'y'))

    result = []
    radix = caf['CAF_RADIX'].value
    rawfmt = caf['CAF_RAWFMT'].value
    engfmt = caf['CAF_ENGFMT'].value
    caps = [row for row in caf.table.scos.cap.rows
            if row['CAP_NUMBR'].value == caf['CAF_NUMBR'].value]
    for caprow in caps:
        raw = caprow['CAP_XVALS'].value
        if rawfmt == NumericFormatType.UNSIGNEDINT:
            raw = radix.convert(raw)
        else:
            raw = rawfmt.convert(raw)
        eng = engfmt.convert(caprow['CAP_YVALS'].value)
        result.append(Point(raw, eng))
    return result
