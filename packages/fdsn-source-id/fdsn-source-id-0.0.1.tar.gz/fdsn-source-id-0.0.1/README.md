# FDSN SourceID

Python library for handling FDSN Source Identifiers

## Getting Started

### Installation

```shell
pip install fdsn-source-id
```

#### Usage

```python
from fdsn_source_id import SourceID

SourceID.from_seed(
    network='IU',
    station='ANMO',
).sourceid  # 'FDSN:IU_ANMO'
```
