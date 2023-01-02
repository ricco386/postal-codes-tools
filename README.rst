Postal Codes Tools
##################

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

Library that helps working with different postal codes. Purpose of this library is to validate string
if it matches the postal code format.

Postal code format checking is based on European Central Bank - `List of postal code formatting rules and regular
expressions per country <https://www.ecb.europa.eu/stats/money/aggregates/anacredit/shared/pdf/List_postal_code_formatting_rules_and_regular_expressions.xlsx>`_
spreadsheet.


Installation
------------

Install the released version::

    pip install postal-codes-tools

Development
-----------

**We look forward to any kind of improvements and support for new postal codes.**

Clone a repository locally and make sure you work in your own branch and once you are happy with the functionality
create pull request. All new code should be covered with tests. We try to use test driven development for the project.

**If you find a bug feel free to create an issue with description**, how ever we appreciate even more if you create failing test.

Release
-------

Release is done via `twine <https://pypi.org/project/twine/>`_. The whole package is uploaded in the form of .dist file.

To create .dist file use command::

    python setup.py sdist bdist_wheel

Now our binary .dist file is created, now we need to upload it using the below command::

    python -m twine dist/*

Alternatively if you want to selfhost in a custom PyPI repo you can also upload there as well::

    python -m twine upload--repository-url https://gitlab.com/custom/repo/path dist/* --cert /custom/cert


Testing
=======

Tests are written in pytest and stored in tests directory. Library has 100% test coverage.
**If you found an error, write a failing test first.**

Run the tests by following command::

    pytest postal_codes_tools
