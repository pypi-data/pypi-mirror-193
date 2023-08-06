# test_project_python

This project contains a dummy python project to
- test how packaging works for python
  - using the `setuptools`  module
    - see the comments in the `setup.py` file for more references and information
  - when uploading to https://test.pypi.org/ and/or https://pypi.org/
    - references describing basic packaging information:
      - [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
      - [Python: Creating a pip installable package](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/)
      - [GPG signing - how does that really work with PyPI?](https://github.com/pypa/twine/issues/157)
      - [Packaging and distributing projects](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
    - references describing more advanced packaging capabilities:
      - [Packaging namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/)
      - [Creating and discovering plugins](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/)
      - [Packaging binary extensions](https://packaging.python.org/en/latest/guides/packaging-binary-extensions/)
    - packaging.python.org landing page: [Python Packaging User Guide](https://packaging.python.org/en/latest/)
      - maintained by [Python Packaging Authority](https://www.pypa.io/en/latest/)

## Project Structure

Note that some of the files below are configuration/build/binary files auto-generated after running commands to set up the package locally, and are NOT included in the repo:
- the `python3 setup.py sdist` commands creates
  - `dist/test-project-0.0.0.tar.gz`
  - `test_project.egg-info` (and nested contents)
- the `python3 setup.py bdist_wheel` command creates
  - `dist/test_project-0.0.0-py3-none-any.whl`
  - `build/bdist.OPERATINGSYSTEMNAME-moreoperatingsysteminfo`
  - `build/lib/`(and nested contents)
  - `test_project.egg-info` (and nested contents)
- the `python3 setup.py bdist_wheel` command creates
  - `build/bdist.OPERATINGSYSTEMNAME-moreoperatingsysteminfo`
  - `build/lib/`(and nested contents)
  - `test_project.egg-info` (and nested contents)

Also note that running python files as modules locally creates a `__pycache__` directory and `.pyc` file nested inside the `__pycache__` directory (which were manually excluded from the structure below) for that corresponding module!
- note that this
  - only happens when running `python3 -m path.to.module.name`
  - does NOT happen when running `python3 path/to/module/name.py`


(structure taken from the output of the `tree` command run from the `test-project/python` directory)
```
.
├── README.md
├── build
│   ├── bdist.OPERATINGSYSTEMNAME-moreoperatingsysteminfo
│   └── lib
│       ├── package_a
│       │   ├── __init__.py
│       │   ├── module_a.py
│       │   ├── module_b.py
│       │   ├── module_c.py
│       │   ├── module_d.py
│       │   └── module_e.py
│       ├── package_b
│       │   ├── __init__.py
│       │   ├── module_a.py
│       │   ├── module_b.py
│       │   ├── module_c.py
│       │   ├── module_d.py
│       │   └── module_e.py
│       ├── package_c
│       │   ├── __init__.py
│       │   ├── module_a.py
│       │   ├── module_b.py
│       │   ├── module_c.py
│       │   ├── module_d.py
│       │   └── module_e.py
│       └── test_project_python
│           ├── __init__.py
│           └── __main__.py
├── dist
│   ├── test-project-0.0.0.tar.gz
│   └── test_project-0.0.0-py3-none-any.whl
├── make_nested_py_modules.sh
├── package_a
│   ├── __init__.py
│   ├── module_a.py
│   ├── module_b.py
│   ├── module_c.py
│   ├── module_d.py
│   ├── module_e.py
│   ├── subpackage_a
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   ├── subpackage_b
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   └── subpackage_c
│       ├── a.py
│       ├── b.py
│       ├── c.py
│       ├── d.py
│       └── e.py
├── package_b
│   ├── __init__.py
│   ├── module_a.py
│   ├── module_b.py
│   ├── module_c.py
│   ├── module_d.py
│   ├── module_e.py
│   ├── subpackage_a
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   ├── subpackage_b
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   └── subpackage_c
│       ├── a.py
│       ├── b.py
│       ├── c.py
│       ├── d.py
│       └── e.py
├── package_c
│   ├── __init__.py
│   ├── module_a.py
│   ├── module_b.py
│   ├── module_c.py
│   ├── module_d.py
│   ├── module_e.py
│   ├── subpackage_a
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   ├── subpackage_b
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   └── subpackage_c
│       ├── a.py
│       ├── b.py
│       ├── c.py
│       ├── d.py
│       └── e.py
├── setup.py
├── test_project.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   └── top_level.txt
└── test_project_python
    ├── __init__.py
    ├── __main__.py
```

## Releases

See the [latest release](https://github.com/shailshouryya/test-project/releases/tag/0.0.1-python) from the [releases page](https://github.com/shailshouryya/test-project/releases)
