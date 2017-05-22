kwconfig
=============

.. toctree::
   :maxdepth: 2

| Richard Wen
| rrwen.dev@gmail.com

A Python module for managing config files in keyword style json format.

::
  
  from kwconfig import kwconfig
  config = kwconfig('config.json')

Install
-------

1. Install `Python <https://www.python.org/downloads/>`_
2. Install `kwconfig <https://pypi.python.org/pypi/kwconfig>`_ via ``pip``

::
  
  pip install kwconfig

Usage
-----

.. code-block:: python
  
  import kwconfig
  
  # Specify a file path for creating kwconfig object
  config = kwconfig.manage('config.json')
  
For more details on module usage, see the example in `kwconfig.manage`_.

Modules
-------

.. automodule:: kwconfig
   :members:
   