#!/usr/bin/python3

import unittest
import os
import requests
import warnings

def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test

class TestPassword(unittest.TestCase):
    '''A class to represent the model'''
    
    def testFile(self):
        self.assertTrue(os.path.isfile('geckodriver'))
        self.assertTrue(os.path.isfile('tempMailList.cvs'))
    
    @ignore_warnings
    def testOnline(self):
        self.assertEqual(str(requests.get('https://temp-mail.org/en/change')), '<Response [200]>')

if __name__ == '__main__':
    unittest.main()
