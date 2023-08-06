# PySpark Helpers

A collection of tools to help when developing PySpark applications

## Installation

With pip
```
pip install pyspark_helpers
```

With poetry
```
poetry add pyspark_helpers
```

## Usage

### Auto Generate PySpark Schemas from JSON examples

Through cli:

```sh
python -m pyspark_helpers.schema
# OR with script
psh-schema-from-json --path ./tests/data/schema/array.json --output ./results/array_schema.json
```

Or programatically

```py
from pyspark_helpers.schema import schema_from_json, bulk_schema_from_jsom
from pathlib import Path

data_dir = "data/json"


## One file
schema = schema_from_json(f"{data_dir}/file.json")

print(schema)

## A whole directory
files = [Path(f) for f in Path.glob(f"{data_dir}/*.json")]
schemas = bulk_schema_from_jsom(files)

for _file, schema in zip(files, schemas):
    print(_file.name, schema)
```
