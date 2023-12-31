# Drifterdata2CSV

Extract metadata from driftViewer software output NetCDF's

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-May%2C%2030%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```bash
pip install netCDF4
```

or

```bash
pip install -r requirements.txt
```

```python
import os
import glob
import csv
from netCDF4 import Dataset
```

## How to run

```python
input_directory = './DrifterDATA'
output_file = 'DATA.csv'

process_netcdf_files(input_directory, output_file)
```
