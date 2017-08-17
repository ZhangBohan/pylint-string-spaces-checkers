# Pylint String Checkers

Additional string checkers for [Pylint](https://pylint.org).

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
