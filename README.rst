Postal Codes Tools
##################

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

Library that helps working with different postal codes. Purpose of this library is to validate string
if it matches the postal code format.

Postal code format checking is based on European Central Bank - `List of postal code formatting rules and regular
expressions per country <https://www.ecb.europa.eu/stats/money/aggregates/anacredit/shared/pdf/List_postal_code_formatting_rules_and_regular_expressions.xlsx>`_
spreadsheet version 1.1.

Intention of the library is to keep version number same as the ECB spreadsheet, eg. v1.1.0, so it is easy the track
regex and ECB changes in the spreadsheet change log. Just the last number, eg. v1.1.2 can change with bug fixes and
updates.


Installation
------------

Install the released version::

    pip install postal-codes-tools

Usage
-----

Basic usage is to verify if the postal code has correct format:

    >>> from postal_codes_tools.postal_codes import verify_postal_code_format
    >>> verify_postal_code_format(country_iso_code="US", postal_code="00716-9999")
    True

Certain countries does not heave posta code, library also provides a check if a country does have
postal code. You can also get the whole list of countries does not heave posta code:

    >>> from postal_codes_tools.postal_codes import country_without_postal_code, has_postal_code
    >>> country_without_postal_code("DE")
    False
    >>> country_without_postal_code("AE")
    True
    >>> has_postal_code("DE")
    True
    >>> has_postal_code("AE")
    False
    >>>
    >>> from postal_codes_tools.postal_codes import get_countries_without_postal_code
    >>> get_countries_without_postal_code()
    ('AE', 'SB', 'GY', 'UG', 'SL', 'KM', 'CK', 'UM', 'KI', 'TK', 'BO', 'DJ', 'GD', 'BQ', 'GQ', 'CF', 'MR', 'SY', 'SX', 'GH', 'ST', 'ZW', 'BZ', 'BJ', 'RW', 'BI', 'AO', 'TL', 'CD', 'CM', 'QA', 'SC', 'TV', 'KP', 'AW', 'CG', 'TD', 'XX', 'BV', 'ML', 'TG', 'ER', 'FJ', 'TO', 'BS', 'GA', 'CI', 'YE', 'CW', 'DM', 'SR', 'VU', 'GM', 'BW')


Since version 1.1 of the ECB spreadsheet, ECB does not define countries without postal code, they just gave them
default regex string `^.{1,255}$`, how ever some of those has an example of posta codes. List of countires without
postal code matches the list of default regex without an example of postal code.

Library provide a map of territories, so you can easily find out to which country they belong. If the country code
is not in the map, original country code is returned. For example Martinique (ISO2 country code: MQ) is overseas
department of France in the Caribbean:

    >>> from postal_codes_tools.mappers import territory_to_parent_mapper
    >>> territory_to_parent_mapper('MQ')
    'FR'
    >>> territory_to_parent_mapper('FR')
    'FR'

Library provides a function to get the regex used for postal code verification and also supports strict postal code
checks for territories:

    >>> from postal_codes_tools.postal_codes import get_postal_code_regex
    >>> get_postal_code_regex('US')
    '^\\d{5}(-\\d{4})?$'
    >>> get_postal_code_regex('MQ')
    '^\\d{5}$'
    >>> get_postal_code_regex('MQ', strict=True)
    '^972\\d{2}$'


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
