{{ cookiecutter.package_name.split('.') | map('capitalize') | join(' ') }}
{{ "=" * cookiecutter.package_name.__len__() }}

{{ cookiecutter.description }}

Build Status
------------

.. image:: https://travis-ci.org/seantis/{{ cookiecutter.package_name }}.png
  :target: https://travis-ci.org/seantis/{{ cookiecutter.package_name }}
  :alt: Build Status

Coverage
--------

.. image:: https://coveralls.io/repos/seantis/{{ cookiecutter.package_name }}/badge.png?branch=master
  :target: https://coveralls.io/r/seantis/{{ cookiecutter.package_name }}?branch=master
  :alt: Project Coverage

Latests PyPI Release
--------------------
.. image:: https://pypip.in/v/{{ cookiecutter.package_name }}/badge.png
  :target: https://crate.io/packages/{{ cookiecutter.package_name }}
  :alt: Latest PyPI Release

License
-------
{{ cookiecutter.package_name }} is released under GPLv2
