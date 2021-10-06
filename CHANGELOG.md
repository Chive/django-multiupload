# Change Log

## [0.6.1](https://github.com/Chive/django-multiupload/tree/0.6.1) (2021-10-06)


### Maintenance
* Ensure upload to PyPI is possible :-)

[Full Changelog](https://github.com/Chive/django-multiupload/compare/0.6.0...0.6.1)


## [0.6.0](https://github.com/Chive/django-multiupload/tree/0.6.0) (2021-10-06)


### Fix
* Proper handling of non-required fields [#46](https://github.com/Chive/django-multiupload/pull/46) and [#47](https://github.com/Chive/django-multiupload/pull/47)
* Fix issue with widget rendering for Django >= 2.1 [#32](https://github.com/Chive/django-multiupload/pull/32)

### Maintenance
* Update supported versions [#45](https://github.com/Chive/django-multiupload/pull/45)
* Add testing utilities [#48](https://github.com/Chive/django-multiupload/pull/48)

[Full Changelog](https://github.com/Chive/django-multiupload/compare/0.5.2...0.6.0)


## [0.5.2](https://github.com/Chive/django-multiupload/tree/0.5.2) (2016-10-14)

### New
* Support for specific media types in inputs (with dedicated field for images)

[Full Changelog](https://github.com/Chive/django-multiupload/compare/0.5.1...0.5.2)

## [0.5.1](https://github.com/Chive/django-multiupload/tree/0.5.1) (2016-04-25)

### Fix
* `MultiFileField` can now accept empty values when required is `False`

[Full Changelog](https://github.com/Chive/django-multiupload/compare/0.5...0.5.1)

## [0.5](https://github.com/Chive/django-multiupload/tree/0.5) (2015-06-14)

### New
* Add tests & integration with Travis CI
* Mark as Python3 compatible

[Full Changelog](https://github.com/Chive/django-multiupload/compare/0.4...0.5)

## [0.4](https://github.com/Chive/django-multiupload/tree/0.4) (2015-06-13)

### New
* Add two example usages
* Add changelog
* Add authors file

### Change
* Improved usage instrutions in README

### Fix
* Fix form validation when checking for maximum file size
* Fix the type of the return value from ``value_from_datadict`` when ``getlist`` is not a method of the ``files`` parameter.

[Full Changelog](https://github.com/Chive/django-multiupload/compare/0.3...0.4)

## [0.3](https://github.com/Chive/django-multiupload/tree/0.3) (2014-07-15)

### Fix
* Fix empty form object handling (no files submitted)

[Full Changelog](https://github.com/Chive/django-multiupload/compare/0.2...0.3)

## [0.2](https://github.com/Chive/django-multiupload/tree/0.2) (2014-07-06)

### Change
* Update README


### Fix
* Fix package config

[Full Changelog](https://github.com/Chive/django-multiupload/compare/0.1...0.2)

## [0.1](https://github.com/Chive/django-multiupload/tree/0.1) (2014-07-05)

### New
* Initial Release

[Full Changelog](https://github.com/Chive/django-multiupload/commit/8ef0df5506dc213714f52ce5801f2c41452e3acc)
