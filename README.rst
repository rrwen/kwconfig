kwconfig
========

| Richard Wen
| rrwen.dev@gmail.com

* `Documentation <https://rrwen.github.io/kwconfig>`_
* `PyPi Package <https://pypi.python.org/pypi/kwconfig>`_

A Python module for managing config files in keyword style json format.


Install
-------

1. Install `Python <https://www.python.org/downloads/>`_
2. Install `kwconfig <https://pypi.python.org/pypi/kwconfig>`_ via ``pip``

::
  
  pip install kwconfig
  
For the latest developer version, see `Developer Install`_.
  
Usage
-----

.. code-block:: python
  
  import kwconfig
  
  # Specify a file path for creating kwconfig object
  config = kwconfig.manage('config.json', defaults={'key0': 'value0'})
  
  # Update the config file with a key and value dict
  config.update({'key1': 'value1', 'key2': 'value2'})
  
  # Add a keyword dict to existing config file
  # If a key exists, it will be updated
  # If a key does not exist, it will be added
  other_config = {'key3': 'value3'}
  other_config = config.add(other_config)
  
  # Write new values using keyword dict
  config.overwrite({
    'new_key1': 'new_value1',
    'new_key2': 'new_value2'
  })
  
  # Obtain a dict of the config file contents
  kw = config.read()
  
  # Remove the key named "key1"
  config.remove('key1')
  
  # Reset to defaults
  config.reset()
  
For more usage details, see the `Documentation <https://rrwen.github.io/kwconfig>`_.

Developer Notes
---------------

Developer Install
*****************

Install the latest developer version with ``pip`` from github::
  
  pip install git+https://github.com/rrwen/kwconfig
  
Install from ``git`` cloned source:

1. Ensure `git <https://git-scm.com/>`_ is installed
2. Clone into current path
3. Install via ``pip``

::

  git clone https://github.com/rrwen/kwconfig
  cd kwconfig
  pip install . -I
  
Tests
*****

1. Ensure `unittest <https://docs.python.org/2.7/library/unittest.html>`_ is available
2. Run tests

::
  
  pip install . -I
  python -m unittest

Documentation Maintenance
*************************

1. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`_ is installed ``pip install -U sphinx``
2. Update the documentation in ``docs/``

::
  
  pip install . -I
  sphinx-build -b html docs/source docs
  
Upload to github
****************

1. Ensure `git <https://git-scm.com/>`_ is installed
2. Add all files and commit changes
3. Push to github

::
  
  git add .
  git commit -a -m "Generic update"
  git push
  
Upload to PyPi
**************

1. Ensure `twine <https://pypi.python.org/pypi/twine>`_ is installed ``pip install twine``
2. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`_ is installed ``pip install -U sphinx``
3. Delete ``dist`` directory
4. Update the version ``kwconfig.py``
5. Update the documentation in ``docs/``
6. Create source distribution
7. Upload to `PyPi <https://pypi.python.org/pypi>`_

::
  
  pip install . -I
  sphinx-build -b html docs/source docs
  python setup.py sdist
  twine upload dist/*
  