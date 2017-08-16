# -*- coding: utf-8 -*-

from os import remove
from unittest import TestCase
from tempfile import NamedTemporaryFile

import kwconfig

class manageTest(TestCase):

  def setUp(self):
    tempfile = NamedTemporaryFile()
    self.in_path = str(tempfile.name)
    tempfile.close()
    
  def test_command(self):
    manage = kwconfig.manage(self.in_path, defaults={})
    with self.assertRaises(SystemExit):
      manage.command(['-h'], i=0)
    with self.assertRaises(SystemExit):
      manage.command(['-v'], i=0)
    with self.assertRaises(SystemExit):
      manage.command(['-s', 'new_key1=newvalue1'], i=0)
    with self.assertRaises(SystemExit):
      manage.command(['-r', 'new_key1'], i=0)
    with self.assertRaises(SystemExit):
      manage.command(['-v'], i=0)
    with self.assertRaises(SystemExit):
      manage.command(['-d'], i=0)
    remove(self.in_path)
  
  def test_reset(self):
    manage = kwconfig.manage(self.in_path, defaults={})
    manage.update({'key1': 'value1'})
    manage.reset()
    self.assertTrue({} == manage.read())
    remove(self.in_path)
    
  def test_read(self):
    manage = kwconfig.manage(self.in_path, defaults={})
    manage.reset()
    expected = {}
    self.assertTrue(expected == manage.read())
    remove(self.in_path)
    
  def test_update(self):
    manage = kwconfig.manage(self.in_path, defaults={})
    manage.reset()
    expected = {'key1': 'value1', 'key2': 'value2'}
    manage.update(expected)
    self.assertTrue(expected == manage.read())
    remove(self.in_path)
    
  def test_add(self):
    manage = kwconfig.manage(self.in_path, defaults={})
    manage.reset()
    expected = {'key2': 'value2', 'key1': 'value1'}
    manage.update({'key1': 'value1'})
    added = manage.add({'key2': 'value2'})
    self.assertTrue(expected == added)
    remove(self.in_path)
    
  def test_overwrite(self):
    manage = kwconfig.manage(self.in_path, defaults={})
    manage.reset()
    expected = {'key3': 'value3', 'key2': 'value2'}
    manage.overwrite(expected)
    self.assertTrue(expected == manage.read())
    remove(self.in_path)
    
  def test_remove(self):
    manage = kwconfig.manage(self.in_path, defaults={})
    manage.reset()
    expected = {'key2': 'value2'}
    manage.update({'key1': 'value1', 'key2': 'value2'})
    manage.remove('key1')
    self.assertTrue(expected == manage.read())
    remove(self.in_path)
    
