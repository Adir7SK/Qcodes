# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import time
from timeit import default_timer as timer

"""
Note: Functions and classes can only be called by particulary names depending on their perposes, 
fx you want the benchmark to measure time, then you'll start its name with time.
When running; the compiler go through all the non-functions(not def) first,
and if there's something to remember, as timeout, the last command (in our example it's the command timeout) will be the one it uses. 
Afterwards it will start compiling the functions
"""


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
   
    timeout = 120.0     #Increases the timeout to 120 sec, instead of the default option - 60 sec.
    def setup(self):
        self.d = {}
        self.len = 50
        for x in range(self.len):
            self.d[x] = None

    #Measures the time to run through the list of keys
    def time_keys(self):
        for key in list(self.d.keys()):
            pass

    #Letting a function that takes longer time to run than the default defines (Should work because we re-defined the timeout)
    #Prints also the time it takes, to make sure there is an agreement
    def time_more_than_default (self):
        start = timer()
        for key in self.d.keys():
            pass
        time.sleep(70)
        elapsed_time = timer() - start
        print (elapsed_time)

    #Measures the run time of a normal for loop
    def time_range(self):
        start = timer()
        for i in range(300000000):
            x=5
            y=x*2
        ell = timer() - start
        print (ell)
        d = self.d
        for key in list(range(self.len)):
            x = d[key]

    #A function that takes more than 120 sec to run, which means that it will fail and print:
    #asv: benchmark timed out (timeout 120.0s).
    def time_destind_to_fail(self):
        time.sleep(200)


class MemSuite:
    #Memory benchmarks, measures the memory
    def mem_list(self):
        return [0] * 256

    def peakmem_list(self):
        [0] * 165536
        
class TimeSuitInharit(TimeSuite):
    #The class will inharit all the functions in TimeSuite
    
    #We change the function time_destind_to_fail so it won't fail.
    def time_destind_to_fail(self):
        start = timer()
        for i in range(300000000):
            x=5
            y=x*2
        ell = timer() - start
        print (ell)
        
    #Creating a new function only for this class
    def time_new(self):
        time.sleep(17.5)
