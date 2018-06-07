import qcodes
from qcodes.instrument_drivers.Keysight.Keysight_34465A import Keysight_34465A
import timeit

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    timeout=120
    timer = timeit.default_timer
    
    def setup(self):
        self.key = Keysight_34465A('name', 'USB0::0x2A8D::0x0101::MY54505388::INSTR')

    def teardown(self):
        self.key.close()

    def time_keyEl(self):
        self.key.NPLC.get()

    def time_keyEl100(self):
        self.key.NPLC(100)
        self.key.volt()

    def time_keyEl10(self):
        self.key.NPLC(10)
        self.key.volt()
