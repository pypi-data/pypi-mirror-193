===============
Release History
===============

v0.3.0 (2023-02-22)
-------------------

- Improve the tests to start the ``test-socket-server`` within the fixture.
- Update pre-commit config.
- Added Timeout Exception class and raised an exception in put function if a
  signal does not reach a given position within a limited timeout period.
- Added a CI configuration to publish the package to PyPI.

v0.2.0 (2023-01-26)
-------------------

- Add ophyd classes for ATF and the corresponding tests.
- Improve CI configs.


v0.1.0 (2023-01-25)
-------------------

Initial release with basic functionality.
