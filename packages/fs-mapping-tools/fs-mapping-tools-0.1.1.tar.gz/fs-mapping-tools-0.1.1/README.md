# Formula Student Mapping Tools

[![Tests status](./reports/badges/tests.svg)](http://htmlpreview.github.io/?https://github.com/erlete/fs-mapping-tools/blob/dev/reports/data/tests/index.html) [![Coverage Status](https://coveralls.io/repos/github/erlete/fs-mapping-tools/badge.svg)](https://coveralls.io/github/erlete/fs-mapping-tools) [![Linter status](./reports/badges/linter.svg)](http://htmlpreview.github.io/?https://github.com/erlete/fs-mapping-tools/blob/dev/reports/data/linter/index.html)


A set of simple utilities for track mapping, designed for Formula Student autonomous events.

## Motivation

This library is created in order to provide with a normalized model for track mapping processes.

## Implementations

* `cones`: module containing cone mapping utilities.
  * `Cone`: cone representation class. Allows categorization and plotting. Works just like a `Coordinate` instance, but with a linked type.
  * `ConeArray`: cone organization class. Allows categorization, collection and plotting. List-like behavior, but with enforced type rules.

It is intended for future releases to implement ROS custom messages for all classes in this repository.
