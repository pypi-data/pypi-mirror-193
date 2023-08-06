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
    'version': '0.2.4a0',
    'description': 'Pinecone Datasets lets you easily load datasets into your Pinecone index.',
    'long_description': '# Pinecone Datasets\n\n## Usage\n\nYou can use Pinecone Datasets to load our public datasets or with your own dataset.\n\n### Loading Pinecone Public Datasets\n\n```python\nfrom pinecone_datasets import list_datasets, load_dataset\n\nlist_datasets()\n# ["cc-news_msmarco-MiniLM-L6-cos-v5", ... ]\n\ndataset = load_dataset("cc-news_msmarco-MiniLM-L6-cos-v5")\n\ndataset.head()\n\n# Prints\n ┌─────┬───────────────────────────┬─────────────────────────────────────┬───────────────────┬──────┐\n │ id  ┆ values                    ┆ sparse_values                       ┆ metadata          ┆ blob │\n │ --- ┆ ---                       ┆ ---                                 ┆ ---               ┆ ---  │\n │ str ┆ list[f32]                 ┆ struct[2]                           ┆ struct[3]         ┆      │\n ╞═════╪═══════════════════════════╪═════════════════════════════════════╪═══════════════════╪══════╡\n │ 0   ┆ [0.118014, -0.069717, ... ┆ {[470065541, 52922727, ... 22364... ┆ {2017,12,"other"} ┆ .... │\n │     ┆ 0.0060...                 ┆                                     ┆                   ┆      │\n └─────┴───────────────────────────┴─────────────────────────────────────┴───────────────────┴──────┘\n```\n\n\n### Iterating over a Dataset documents\n\n```python\n\n# List Iterator, where every list of size N Dicts with ("id", "metadata", "values", "sparse_values")\ndataset.iter_documents(batch_size=n) \n```\n\n### upserting to Index\n\n```bash\npip install pinecone-client\n```\n\n```python\nimport pinecone\npinecone.init(api_key="API_KEY", environment="us-west1-gcp")\n\npinecone.create_index(name="my-index", dimension=384, pod_type=\'s1\')\n\nindex = pinecone.Index("my-index")\n\n# Or: Iterating over documents in batches\nfor batch in dataset.iter_documents(batch_size=100):\n    index.upsert(vectors=batch)\n```\n\n#### upserting to an index with GRPC\n\nSimply use GRPCIndex and do:\n\n```python\nindex = pinecone.GRPCIndex("my-index")\n\n# Iterating over documents in batches\nfor batch in dataset.iter_documents(batch_size=100):\n    index.upsert(vectors=batch)\n```\n',
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
