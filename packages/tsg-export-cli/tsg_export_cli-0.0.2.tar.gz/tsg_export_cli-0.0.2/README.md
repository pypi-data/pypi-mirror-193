# TSG Export CLI
Provides access to the `tsg-cli` command that exports tsg data

## Installation
Due to a direct dependency, the installation requires two steps. Replace `pip` with `pip3` if `pip` is unrecognised or bound to python2.
```bash
pip install git+https://github.com/CSIRO-GeoscienceAnalytics/tsg-xr@8aea5c890daa4663e5d7251f2f0ca584b61e2237
pip install tsg-export-cli
```

## Usage
### Producing Scalar Dumps
```bash
tsg-cli export-csvs --help
```

### Producing Borehole Imagery
A downsampling factor of `q` results in a performance boost and quality reduction of `q²`.

If images are meant for human viewing use the depth delta (`-d`) to get smaller and wider images. 0.5m of core per image is a good start.
```bash
tsg-cli export-images --help
```

## For Development
## Package Build & Upload
```bash
python -m build && python -m twine upload --repository pypi dist/*
```
