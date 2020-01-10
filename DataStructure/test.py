#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/unittest.html
https://www.geeksforgeeks.org/unit-testing-python-unittest/
Created on Sun Sep 29 17:07:37 2019
@author: administrator
"""
import unittest

class SimpleTest(unittest.TestCase):
    
    
        
    # Returns True if the string contains 4 a. 
    def test_strings_a(self): 
        self.assertEqual( 'a'*4, 'aaaa') 
  
    # Returns True if the string is in upper case. 
    def test_upper(self):         
        self.assertEqual('foo'.upper(), 'FOO') 
  
    # Returns TRUE if the string is in uppercase 
    # else returns False. 
    def test_isupper(self):         
        self.assertTrue('FOO'.isupper()) 
        self.assertFalse('Foo'.isupper()) 
  
    # Returns true if the string is stripped and  
    # matches the given output. 
    def test_strip(self):         
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks') 
  
    # Returns true if the string splits and matches 
    # the given output. 
    def test_split(self):         
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world']) 
        with self.assertRaises(TypeError): 
            s.split(2)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

  
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
        
    if __name__=='__main__':
        unittest.main()
