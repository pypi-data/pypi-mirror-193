"""Synthetic parameter handling classes and functions"""

from .concrete import Parameter


class SyntheticParameterDefinition:
    """The definition of a synthetic parameter"""
    def __init__(self, pcf):
        self.inputs = set()
        """The set of parameters (by ID) that are inputs/dependencies to this
        synthetic parameter.

        This set will be used to determine in what packets this parameter will
        magically appear."""
        self.pcf = pcf

    def evaluate(self, packet):
        """Evaluate the definition of this parameter in the context of this ``packet``

        ``packet`` should be derived from ``PacketInterface`` (or otherwise
        satisfy the interface).

        Returns a ``SyntheticParameterInstance`` containing the respective ``raw``
        and ``eng`` values.
        """
        raise NotImplementedError()

    def parse(self, stream):
        """Parse the parameter definition from ``stream``"""
        raise NotImplementedError()


class DynamicSyntheticParameter(SyntheticParameterDefinition):
    """A dynamic synthetic parameter (PCF_NATUR = D)"""
    # TODO #7 - that's a big project on its own right here:
    # this should use EGOS-MCS-S2K-SUM-0019 to parse the
    # OL definition of such a synthetic parameter

    def evaluate(self, packet):
        # for now all we do is to provide an instance that's just plain invalid
        return InvalidSyntheticParameterInstance(packet, self.pcf)

    def parse(self, stream):
        pass


class SyntheticParameterInstance(Parameter):
    """A synthetic parameter instance with a fixed value"""
    def __init__(self, rawvalue, packet, pcf):
        super().__init__(packet, pcf)
        self._raw_value = rawvalue

    def get_raw(self):
        return self._raw_value


class InvalidSyntheticParameterInstance(SyntheticParameterInstance):
    """A generic invalid parameter instance"""
    def __init__(self, packet, pcf):
        super().__init__(0, packet, pcf)

    def calculate_validity(self):
        return False
