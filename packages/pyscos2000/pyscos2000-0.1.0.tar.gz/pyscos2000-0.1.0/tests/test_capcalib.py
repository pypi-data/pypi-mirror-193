"""Test case to verify the CAF/CAP calibration"""
import unittest
from pathlib import Path

from pyscos2000 import SCOS, PacketInterface, Parameter


class TestablePacket(PacketInterface):
    """A packet type used for unit testing"""
    def __init__(self, scos, spid, parameters=None):
        super().__init__()
        pids = [r for r in scos.pid if r['PID_SPID'].value == spid]
        assert len(pids) == 1
        self.pid = pids[0]
        self.parameters = {}
        if parameters is not None:
            for name, value in parameters:
                pcf = self.pid.scos.pcf.get(name)
                self.parameters[name] = TestableParameter(value, self, pcf)

    def get(self, item):
        return self.parameters[item]

    def get_all(self, item):
        return [self.parameters[item]]

    def has(self, item):
        return item in self.parameters

    def __len__(self):
        return len(self.parameters)

    def iter(self):
        for value in self.parameters.values():
            yield value


class TestableParameter(Parameter):
    """A packet parameter type used for testing"""
    def __init__(self, value, packet, pcf):
        super().__init__(packet, pcf)
        assert isinstance(value, bytes)
        self.value = value

    def get_raw(self):
        return self.paramtype.unpack(self.value)

    def get_hex(self):
        return self.value.hex()


class CAPCalibTest(unittest.TestCase):
    def setUp(self):
        self.scos = SCOS(Path(__file__).parent / 'capcalib')
        self.scos.check()

    def test_canary(self):
        self.assertFalse(True)

    def test_simple1(self):
        """Test simple interpolation"""
        packet = TestablePacket(self.scos, 15,
                                [('PCF01', b'\x05')])
        self.assertEqual(packet['PCF01'].raw, 5)
        self.assertEqual(packet['PCF01'].eng, 2.5)

    def test_simple2(self):
        """Test simple interpolation"""
        packet = TestablePacket(self.scos, 15,
                                [('PCF01', b'\x0b')])
        self.assertEqual(packet['PCF01'].raw, 11)
        self.assertEqual(packet['PCF01'].eng, 4.5)

    def test_exact1(self):
        """Test an exactly matching point"""
        packet = TestablePacket(self.scos, 15,
                                [('PCF01', b'\x08')])
        self.assertEqual(packet['PCF01'].raw, 8)
        self.assertEqual(packet['PCF01'].eng, 2)

    def test_exact2(self):
        """Test an exactly matching point"""
        packet = TestablePacket(self.scos, 15,
                                [('PCF01', b'\x01')])
        self.assertEqual(packet['PCF01'].raw, 1)
        self.assertEqual(packet['PCF01'].eng, 0)

    def test_extrapolate_fail1(self):
        """Test a failing (because not defined) extrapolation"""
        packet = TestablePacket(self.scos, 15,
                                [('PCF01', b'\x0f')])
        self.assertEqual(packet['PCF01'].raw, 15)
        self.assertEqual(packet['PCF01'].eng, None)

    def test_extrapolate_fail2(self):
        """Test a failing (because not defined) extrapolation"""
        packet = TestablePacket(self.scos, 15,
                                [('PCF01', b'\x00')])
        self.assertEqual(packet['PCF01'].raw, 0)
        self.assertEqual(packet['PCF01'].eng, None)

    def test_extrapolate1(self):
        """Test a succeeding extrapolation (beyond upper)"""
        packet = TestablePacket(self.scos, 15,
                                [('PCF02', b'\x0f')])
        self.assertEqual(packet['PCF02'].raw, 15)
        self.assertEqual(packet['PCF02'].eng, 2.5)

    def test_extrapolate2(self):
        """Test a succeeding extrapolation (below lower)"""
        packet = TestablePacket(self.scos, 15,
                                [('PCF02', b'\x00')])
        self.assertEqual(packet['PCF02'].raw, 0)
        self.assertTrue(abs(packet['PCF02'].eng + 1.6666) < 0.0001)
