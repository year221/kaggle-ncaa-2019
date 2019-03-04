# kaggle-ncaa-2019

Modules and Sample Aanlysis of NCAA 2019 data in Kaggle
This repo includes 
- Files for the package `ncaa2019`
- Sample analysis under notebook folder


# Install Package

The package requires Python package `kaggle`, with token store at `~/.kaggle/kaggle.json`.
See [https://github.com/Kaggle/kaggle-api] for details.

To install the package, clone the repo and run
```
python setup.py install
```
The package name is `ncaa2019`

# Functionality

Only a `DataSet` class is currently provided to load and cache data. 
See [notebook/DataOverview] for an example of how to use the package.

```
# Load package
from ncaa2019 import DataSet

# Set up
ds = DataSet()
# Default cache dir is at ~/kaggle-ncaa-2019-data. 
# Set your own dir by running DataSet('new cache dir path')

# list data set
ds.list_raw_keys()

# Load a table
ds.get_raw_data('r_compact_result')
```



