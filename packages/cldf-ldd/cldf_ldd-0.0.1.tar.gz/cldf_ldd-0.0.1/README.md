# cldf-ldd

CLDF schemata for language description and documentation.

![License](https://img.shields.io/github/license/fmatter/cldf-ldd)
[![PyPI](https://img.shields.io/pypi/v/cldf-ldd.svg)](https://pypi.org/project/cldf-ldd)
![Versions](https://img.shields.io/pypi/pyversions/cldf-ldd)

Details are found in [components](src/cldf_ldd/components).
Every component can be used as follows when creating a CLDF dataset:

```python
from cldf_ldd import StemTable
...
args.writer.cldf.add_component(StemTable)
...
args.writer.objects["stems.csv"].append({...})
```