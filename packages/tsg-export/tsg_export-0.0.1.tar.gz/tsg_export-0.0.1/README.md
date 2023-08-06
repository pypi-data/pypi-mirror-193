# TSG Export CLI
Provides access to a command `tsg-cli` (TODO?: rename) that exports tsg data

## Installation
TODO: get this on live PyPI instead of just the test PyPI environment

The installation unfortunately required two steps as I'm not sure how to add direct dependencies to PyPI
```bash
pip install git+https://github.com/CSIRO-GeoscienceAnalytics/tsg-xr
py -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ tsg-export
```

## Usage
Refer to the help for more info:
```bash
tsg-cli --help
```


## TODO: REMOVE
build & upload
```bash
cd ../tsg-export-cli-package/ && deactivate && source Scripts/activate && rm -rf dist && py -m build && py -m twine upload --repository testpypi dist/*
```

remove & download
```bash
cd ../testing-cli/ && deactivate && source Scripts/activate && pip uninstall -y tsg-export && py -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ tsg-export && pip list
```