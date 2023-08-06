# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyspark_helpers']

package_data = \
{'': ['*']}

install_requires = \
['delta-spark>=2.2.0,<3.0.0', 'pyspark>=3.3.2,<4.0.0']

entry_points = \
{'console_scripts': ['psh-schema-from-json = pyspark_helpers.schema:main']}

setup_kwargs = {
    'name': 'pyspark-helpers',
    'version': '0.1.3',
    'description': 'A collection of tools to help when developing PySpark applications',
    'long_description': '# PySpark Helpers\n\nA collection of tools to help when developing PySpark applications\n\n## Installation\n\nWith pip\n```\npip install pyspark_helpers\n```\n\nWith poetry\n```\npoetry add pyspark_helpers\n```\n\n## Usage\n\n### Auto Generate PySpark Schemas from JSON examples\n\nThrough cli:\n\n```sh\npython -m pyspark_helpers.schema\n# OR with script\npsh-schema-from-json --path ./tests/data/schema/array.json --output ./results/array_schema.json\n```\n\nOr programatically\n\n```py\nfrom pyspark_helpers.schema import schema_from_json, bulk_schema_from_jsom\nfrom pathlib import Path\n\ndata_dir = "data/json"\n\n\n## One file\nschema = schema_from_json(f"{data_dir}/file.json")\n\nprint(schema)\n\n## A whole directory\nfiles = [Path(f) for f in Path.glob(f"{data_dir}/*.json")]\nschemas = bulk_schema_from_jsom(files)\n\nfor _file, schema in zip(files, schemas):\n    print(_file.name, schema)\n```\n',
    'author': 'Jens Peder Meldgaard',
    'author_email': 'jenspederm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
