Postal Codes Tools
##################

.. image:: https://gitlab.nbs.sk/ofi/postal-codes-tools/badges/master/pipeline.svg
   :alt: pipeline status
   :target: https://gitlab.nbs.sk/ofi/postal-codes-tools/-/pipelines

.. image:: https://gitlab.nbs.sk/ofi/postal-codes-tools/badges/master/coverage.svg
   :alt: coverage report

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

Library that helps working with different postal codes. Purpose of this library is to validate string
if it matches the postal code format.

Installation
------------

Install the released version::

    pip install https://gitlab.nbs.sk/ofi/postal-codes-tools/-/archive/v1.0.0/postal-codes-tools-v1.0.0.zip --trusted-host gitlab.nbs.sk

Alternatively you can install the package latest development version from the git repository::

    pip install https://gitlab.nbs.sk/ofi/postal-codes-tools/-/archive/master/postal-codes-tools-master.zip --trusted-host gitlab.nbs.sk

Development
-----------

**We look forward to any kind of improvements and support for new postal codes.**

Clone a repository locally and make sure you work in your own branch and once you are happy with the functionality
create pull request. All new code should be covered with tests. We try to use test driven development for the project.

**If you find a bug feel free to create an issue with description**, how ever we appreciate even more if you create failing test.


Testing
=======

Tests are written in pytest and stored in tests directory. Library has 100% test coverage.
**If you found an error, write a failing test first.**

Run the tests by following command::

    pytest postal_codes_tools
