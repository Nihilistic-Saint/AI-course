import unittest
from helpers import *
import numpy as np


started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_Python(self):
        self.startTest()
        callpython()
        b=np.load('src/b.npy')
        c=np.zeros((3,4))
        c[0,0]=1
        c[-1,-1]=-1
        #Test correct size
        self.assertTrue(np.size(b)==np.size(c))
        #Check all elements
        self.assertTrue((b==c).all())
        self.endTest()
    
    def startTest(self):
        global started_tests
        started_tests=started_tests+1
        print('\nStart test', started_tests)

    def endTest(self):
        global completed_tests
        print('End test', started_tests)
        completed_tests=completed_tests+1


def completed():
    global completed_tests
    return completed_tests

def started():
    global started_tests
    return started_tests

