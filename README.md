# Pylint String Spaces Checkers

Additional string checkers for [Pylint](https://pylint.org).

[![Build Status](https://travis-ci.org/ZhangBohan/pylint-string-spaces-checkers.svg?branch=master)](https://travis-ci.org/ZhangBohan/pylint-string-spaces-checkers)[![PyPI version](https://badge.fury.io/py/pylint-string-spaces-checkers.svg)](https://badge.fury.io/py/pylint-string-spaces-checkers)

## Install

```
pip install pylint-string-spaces-checkers
```

## Usage

To use the additional string checkers, run Pylint as follows:

```
pylint --load-plugins string_spaces_checkers foo.py
```

## Checkers

### String concatenation spaces

String substitution is often recommended over string concatenation, but most time we just miss the comma, so we should
check if we miss comma between strings
