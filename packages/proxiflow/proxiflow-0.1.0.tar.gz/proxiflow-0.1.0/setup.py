# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proxiflow', 'proxiflow.config', 'proxiflow.core', 'proxiflow.utils']

package_data = \
{'': ['*']}

install_requires = \
['black>=23.1.0,<24.0.0',
 'click>=8.1.3,<9.0.0',
 'numpy>=1.24.2,<2.0.0',
 'polars>=0.16.7,<0.17.0',
 'pyaml>=21.10.1,<22.0.0']

setup_kwargs = {
    'name': 'proxiflow',
    'version': '0.1.0',
    'description': 'Data Preprocessing flow tool in python',
    'long_description': 'Preflow\n=======\n\nPreflow is a data preparation tool for machine learning that performs data cleaning, normalization, and feature engineering.\n\nUsage\n-----\n\nTo use Preflow, install it via `pip` (from test PyPi):\n\n.. code-block:: bash\n\n    pip install --find-links ./wheels --index-url https://test.pypi.org/simple preflow\n\nYou can then call it from the command line:\n\n.. code-block:: bash\n\n    preflow --config-file myconfig.yaml --input-file mydata.csv --output-file cleaned_data.csv\n\nHere\'s an example of a YAML configuration file:\n\n.. code-block:: yaml\n\n    data_cleaning:\n      remove_duplicates: True\n      handle_missing_values:\n        drop: True\n\n    data_normalization:\n      ...\n\n    feature_engineering:\n      ...\n\nThe above configuration specifies that duplicate rows should be removed and missing values should be dropped.\n\nAPI\n---\n\nPreflow can also be used as a Python library. Here\'s an example:\n\n.. code-block:: python\n\n    import polars as pl\n    from preppy.config import Config\n    from preppy.preprocessor import Preprocessor\n\n    # Load the data\n    df = pl.read_csv("mydata.csv")\n\n    # Load the configuration\n    config = Config("myconfig.yaml")\n\n    # Preprocess the data\n    preprocessor = Preprocessor(config)\n    cleaned_df = preprocessor.clean_data(df)\n\n    # Write the output data\n    cleaned_df.write_csv("cleaned_data.csv")\n\nTODO\n----\n\n- [x] Data cleaning\n- [ ] Data normalization\n- [ ] Feature engineering\n\nNote: only data cleaning is currently implemented; data normalization and feature engineering are TODO features.\n',
    'author': 'Martin Tomes',
    'author_email': 'tomesm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
