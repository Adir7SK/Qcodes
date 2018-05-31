import time
from timeit import default_timer as timer
import sys
sys.path.append('/users/adir/Desktop/ASV-project') 
import Experimental as e

class TimeSuite:
   
    timeout = 120.0     #Increases the timeout to 120 sec, instead of the default option - 60 sec.
    def setup(self):
        self.d = {}
        self.len = 50
        for x in range(self.len):
            self.d[x] = None

 
    def time_keys(self):
        for key in list(self.d.keys()):
            pass

    def time_experimental(self):
            e.wait()

    def mem_experimental(self):
        print (e.alphabetic_order("badc gefh"))
        #print (e.unique_chars("Adir"))
        print (e.longest_word("when you are going to some place and notice Somthing"))
