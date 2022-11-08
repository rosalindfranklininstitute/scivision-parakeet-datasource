# scivision-parakeet-datasource
> Provides a data source of curated synthetic cryoEM images from [Parakeet](https://github.com/rosalindfranklininstitute/parakeet) for the scivision framework.

[![Building](https://github.com/rosalindfranklininstitute/scivision-parakeet-datasource/actions/workflows/python-package.yml/badge.svg)](https://github.com/rosalindfranklininstitute/scivision-parakeet-datasource/actions/workflows/python-package.yml)

## Installation

```
pip install git+https://github.com/rosalind-franklin-institute/scivision-parakeet-datasource.git
```

> **_NOTE:_** Because the package needs to be built locally from source and has
some external dependencies you may need to ensure your environment is ready before
running this command. You need to set the location of the CUDA compiler and
possibly G++ and FFTW libraries. For full instructions please see the
installation documentation
[here](https://rosalindfranklininstitute.github.io/parakeet/installation.html).


## Usage

```python
import scivision

cat = scivision.load_dataset("./")

images = cat.parakeet_4v1w_x1.read()

```
