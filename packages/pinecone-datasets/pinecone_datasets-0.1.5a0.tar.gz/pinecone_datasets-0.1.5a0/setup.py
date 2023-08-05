# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pinecone_datasets']

package_data = \
{'': ['*']}

install_requires = \
['fsspec>=2023.1.0,<2024.0.0',
 'gcsfs>=2023.1.0,<2024.0.0',
 'pandas>=1.5.3,<2.0.0',
 'polars>=0.16.4,<0.17.0',
 'protobuf>=3.19.3,<3.20.0',
 'pyarrow>=11.0.0,<12.0.0',
 'pydantic>=1.10.5,<2.0.0',
 's3fs>=2023.1.0,<2024.0.0']

setup_kwargs = {
    'name': 'pinecone-datasets',
    'version': '0.1.5a0',
    'description': 'Pinecone Datasets lets you easily load datasets into your Pinecone index.',
    'long_description': '# Pinecone Datasets\n\n## Usage\n\nYou can use Pinecone Datasets to load our public datasets or with your own dataset.\n\n### Loading Pinecone Public Datasets\n\n```python\nfrom datasets import list_datasets, load_dataset\n\nlist_datasets()\n# ["cc-news_msmarco-MiniLM-L6-cos-v5", ... ]\n\ndataset = load_dataset("cc-news_msmarco-MiniLM-L6-cos-v5")\n\ndataset.head()\n\n# Prints\n ┌─────┬───────────────────────────┬─────────────────────────────────────┬───────────────────┬──────┐\n │ id  ┆ values                    ┆ sparse_values                       ┆ metadata          ┆ blob │\n │ --- ┆ ---                       ┆ ---                                 ┆ ---               ┆ ---  │\n │ str ┆ list[f32]                 ┆ struct[2]                           ┆ struct[3]         ┆      │\n ╞═════╪═══════════════════════════╪═════════════════════════════════════╪═══════════════════╪══════╡\n │ 0   ┆ [0.118014, -0.069717, ... ┆ {[470065541, 52922727, ... 22364... ┆ {2017,12,"other"} ┆ .... │\n │     ┆ 0.0060...                 ┆                                     ┆                   ┆      │\n └─────┴───────────────────────────┴─────────────────────────────────────┴───────────────────┴──────┘\n```\n\n\n\n\n<!-- ### Loading a dataset from file\n\n```python\ndataset = Dataset.from_file("https://storage.googleapis.com/gareth-pinecone-datasets/quora.parquet")\n\ndataset.head()\n```\n\n### Loading a dataset from a local directory \n\nTo load data from a local directory we expect data to be uploaded to the following directory structure:\n\n    .\n    ├── ...\n    ├── path                       # path to where all datasets\n    │   ├── dataset_id             # name of dataset\n    │   │   ├── documents          # datasets documents\n    │   │   │   ├── doc1.parquet  \n    │   │   │   └── doc2.parquet   \n    │   │   ├── queries            # dataset queries\n    │   │   │   ├── q1.parquet  \n    │   │   │   └── q2.parquet   \n    └── ...\n    \nSchema for Documents should be \n```python\n{\n    \'id\': Utf8,                          # Document ID\n    \'values\': List(Float32),             # Desnse Embeddings\n    \'sparse_values\': Struct([            # Sparse Embeddings\n        Field(\'indices\', List(Int32)), \n        Field(\'values\', List(Float32))\n    ])\n    \'metadata\': Struct(...)              # String -> Any key value pairs\n    \'blob\': Any                          # Any (document representation)\n}\n ```\n\nand for queries\n```python\n{\n    \'id\': Utf8,                          # Document ID\n    \'values\': List(Float32),             # Desnse Embeddings\n    \'sparse_values\': Struct([            # Sparse Embeddings\n        Field(\'indices\', List(Int32)), \n        Field(\'values\', List(Float32))\n    ])\n    \'filter\': Struct(...)                # String -> Any key value pairs\n    \'blob\': Any                          # Any (document representation)\n}\n ```\n\n```python\nfrom datasets import Dataset\n\n# Dataset(dataset_id: str = None, path: str = None)\n\ndataset = Dataset("two_docs-edo-edo", path="data/")\n``` -->\n\n### Iterating over a Dataset documents\n\n```python\n\n# List Iterator, where every list of size N Dicts with ("id", "metadata", "values", "sparse_values")\ndataset.iter_documents(batch_size=n) \n```\n\n### upserting to Index\n\n```bash\npip install pinecone-client\n```\n\n```python\nimport pinecone\npinecone.init(api_key="API_KEY", environment="us-west1-gcp")\n\npinecone.create_index(name="my-index", dimension=384, pod_type=\'s1\')\n\nindex = pinecone.Index("my-index")\n\n# Or: Iterating over documents in batches\nfor batch in dataset.iter_documents(batch_size=100):\n    index.upsert(vectors=batch)\n```\n\n#### upserting to an index with GRPC\n\nSimply use GRPCIndex and do:\n\n```python\nindex = pinecone.GRPCIndex("my-index")\n\n# Iterating over documents in batches\nfor batch in dataset.iter_documents(batch_size=100):\n    index.upsert(vectors=batch)\n```\n',
    'author': 'Pinecone',
    'author_email': 'None',
    'maintainer': 'Roy Miara',
    'maintainer_email': 'miararoy@gmail.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
