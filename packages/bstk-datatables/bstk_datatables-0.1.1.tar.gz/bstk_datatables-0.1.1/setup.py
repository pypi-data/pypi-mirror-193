# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bstk_datatables']

package_data = \
{'': ['*']}

install_requires = \
['marshmallow>=3.19.0,<4.0.0']

extras_require = \
{':python_version < "3.10"': ['typing_extensions>=4.5.0,<5.0.0']}

setup_kwargs = {
    'name': 'bstk-datatables',
    'version': '0.1.1',
    'description': 'A polymorphic schema managed semi structured crosslinked data dictionary builder.. BINGO!',
    'long_description': '# Datatables - structured data library based on schemas\n\n[homepage](https://github.com/broadstack-com-au/bstk-datatables)\n\n## Dev\n\n1. `poetry install`\n1. `poetry shell`  \n-- Make changes --\n1. `poetry run pytest`\n1. `poetry run black bstk_datatables`\n1. `poetry run flake8 bstk_datatables`  \n-- Commit & Push --\n\n## Install\n\n`pip install bstk-datatables`\n\n## Overview\n\nDatatables act as an intermediary between [Marshmallow structures](https://marshmallow.readthedocs.io/en/stable/) and user defined data storage structures.  \nIt is designed to provide "just enough" sidechannel structure to facilitate building a dynamic schema, (and connecting with "other" interfaces), without losing the advantages afforded by static Marshmallow schemas.\n\n### Schema\n\nSchema models are;\n\n* `Schema`: A collection of fields and references that make up a partial or complete entry\n* `SchemaField`: A basic instruction container representing a single value\n* `SchemaFieldFormat`: The specific instructions for how the field should be collected, represented, formatted and stored\n* `SchemaValuesError`: The only type of exception raised during schema validation\n\nThese schemas and fields are mapped to equivalent [Marshmallow structures](https://marshmallow.readthedocs.io/en/stable/) which provide the entry value validation mechanisms.. ref: `Schema.process_values()`\n\n### Entry\n\nAn `Entry` is a collection of field values, references data, connector references and schema links.\n\n* `.schemata` is a list of `Schema.code`\'s\n* `.table_id` is a link back to a `Table.uuid`\n* `.references` and `.connector_references` are unrestricted containers. Two containers are provided to seperate "core" references from "free-form" references.\n* `.values` is a dict of `Field.code` => `value` that conform to the listed schemata\n\n### Table\n\nA `Table` corrals one or more `Entry` and shapes them towards one or more `Schema`.\n\n* `.schemata` is a list of `Schema.code`\'s that all entries _must_ inherit\n* `.references` and `.connectors` are unrestricted containers. Two containers are provided to seperate "core" references from "free-form" references (and allows correlation with table entries).\n\n### Marshalling and Persistence\n\nAll core classes (and `Enum`) expose an `export` method which return a dict.  \nThe result of an `export()` can be unpacked and provided to its constructor.  \n\n```python\n\ndef test_entry_export():\n    data = {\n        "uuid": str(uuid4()),\n        "table_id": str(uuid4()),\n        "name": "Data Entry",\n        "references": {"entity_uuid": str(uuid4())},\n        "connector_references": {"connector1": "connector_ref"},\n        "schemata": ["base"],\n        "values": {"base/value1": "XG230"},\n    }\n    entry = Entry(**data)\n    exported = export(entry)\n    assert exported == data\n\n```\n\nThe simplest way to handle data persistence is to encapsulate class instanciation and the `export` method of the relevant class into an ORM or ODM framework.  \n`MergeSchema` do not provide an export mechanism because they are not first-class citizens and are designed to work with established `Schema` structures.\n\n[This test provides an example of how to implement persistence with flat files](./tests/functional/test_persistence_documents.py#106).\n\n## Extras\n\n### MergedSchema\n\nTables and Entries support more than a single schema reference.  \n`MergedSchema` exists to facilitate mutli-schema validation and field ordering.\n\nProvide `Dict[Schema.Code: Schema]` as `schemata` when initialising a `MergedSchema` and it will:\n\n1. Process the schema in order\n1. De-dupe fields with the same code (If a later schema includes a field with the same code as a previously loaded schema - that field will be skipped)\n1. Provide a validation mechanism for entries\n\n### Enum\n\nEnum are used within schemas as de-duped lookups. Multiple schema fields can use the same Enum for shaping values.  \n\nUsage:\n\n1. Provide an `Enum.code` as a `lookup` instead of a `values` list when supplying `SchemaFieldFormat` to a schemafield.\n1. Provide the instanciated `Enum` to `Schema.attach_lookup` on a compiled `Schema` or `MergedSchema`.  \n\n__or__\n\n1. Provide an instanciated `Enum` as a `lookup` instead of a `values` list when supplying `SchemaFieldFormat` to a schemafield.\n',
    'author': 'colin',
    'author_email': 'colin@broadstack.com.au',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
