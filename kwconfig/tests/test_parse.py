# -*- coding: utf-8 -*-

from unittest import TestCase

import kwconfig

class parseTest(TestCase):
  
  def test_example(self):
    argv = ['--key1=value1', '--key2=value2']
    kwdict = kwconfig.parse(argv)
    expected = {'key1': 'value1', 'key2': 'value2'}
    self.assertTrue(expected == kwdict)
    
  def test_singledash(self):
    argv = ['-key1=value1', '-key2=value2']
    kwdict = kwconfig.parse(argv)
    expected = {'key1': 'value1', 'key2': 'value2'}
    self.assertTrue(expected == kwdict)
  
  def test_nodash(self):
    argv = ['key1=value1', 'key2=value2']
    kwdict = kwconfig.parse(argv)
    expected = {'key1': 'value1', 'key2': 'value2'}
    self.assertTrue(expected == kwdict)
  
  def test_valueonly(self):
    argv = ['value1', 'value2']
    with self.assertRaises(Exception):
      kwconfig.parse(argv)
