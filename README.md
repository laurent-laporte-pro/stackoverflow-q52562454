# Project Title


StackOverflow question study: [Avoid package name collision in Python unittest](https://stackoverflow.com/q/52562454/1513933)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

To clone the project from Github, you can do:

```bash
git clone https://github.com/laurent-laporte-pro/stackoverflow-q52562454.git
```

### Prerequisites

To see this study in action, you need Python (version 2 or 3), and (optionally) the [PyTest](https://docs.pytest.org) framework.

Create and activate a [virtualenv](https://virtualenv.pypa.io) an run:

```bash
pip install pytest
```

### Installing

This library in not available on [PyPi](https://pypi.org/), you need to install it from source.

```bash
pip install -e .
```

## Running the samples

The purpose of this question is to understand the behavior of [unittest](https://docs.python.org/3/library/unittest.html) –The standard module used to run unit tests– on a specific project configuration.

You can also try the behavior of [PyTest](https://docs.pytest.org) –A third-party library– to compare the result.

To run unit tests with **unittest**:

```bash
python -m unittest discover tests
```

The problem is that we get an exception:

```

======================================================================
ERROR: package_1.test_module_1 (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: package_1.test_module_1
Traceback (most recent call last):
  ...
ModuleNotFoundError: No module named 'package_1.module_1'
```

To run unit tests with **pytest**:

```bash
pytest tests
```

With PyTest, we have the same kind of error:

```
ImportError while importing test module '.../test_module_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
tests/package_1/test_module_1.py:4: in <module>
    from package_1.module_1 import f
E   ModuleNotFoundError: No module named 'package_1.module_1'
```

This project was made to help understanding and reproducing the Original Poster's (OP) problem.

## Possible solution

A solution is to turn the `tests` directory into a Python package by adding a `__init__.py` file.
And run the `unittest` command by specifying the top level directory of the project:

```bash
python -m unittest discover tests -t .
```

The result is:

```

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

The problem is also resolved with PyTest:

```bash
pytest tests
```

The result is:

```

======================== test session starts ========================
platform darwin -- Python 3.6.1, pytest-3.8.1, py-1.6.0, pluggy-0.7.1
rootdir: /Users/laurentlaporte/workspace/stackoverflow-q52562454, ini
file:
collected 1 item                                                    

tests/package_1/test_module_1.py .                            [100%]

===================== 1 passed in 0.01 seconds ======================
```

## Authors

* **Laurent LAPORTE** - *Initial work* - [GitHub profile](https://laurent-laporte-pro.github.io/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Maggyero](https://stackoverflow.com/users/2326961/maggyero) Original Poster on StackOverflow.
