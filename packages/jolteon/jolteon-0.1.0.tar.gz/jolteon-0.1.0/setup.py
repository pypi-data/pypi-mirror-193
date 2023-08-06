# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jolteon']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.3,<2.0.0',
 'psycopg2-binary>=2.9.5,<3.0.0',
 'pydantic[dotenv]>=1.10.5,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'tabulate>=0.9.0,<0.10.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['jolteon = jolteon.__main__:app']}

setup_kwargs = {
    'name': 'jolteon',
    'version': '0.1.0',
    'description': '',
    'long_description': "![jolteon](https://assets.pokemon.com/assets/cms2/img/pokedex/full/135.png)\n\nAre you a Lightdash user? Have you ever had to change the name of a metric, dimension or model in your dbt project?\n\nIf so, you'd know for sure that adapting the Lightdash charts to these changes is a huge pain.\n\nThis python package aims to partially solve this issue automatically updating the Lightdash database.\n\nIt works pretty well most of the times, but there are still some corner cases when you'll find your charts a little bit different after the migration. Anyway, this package will still save you hours of manual updates.\n\n## How to install Jolteon\n\n```\npip install jolteon\n```\n\n## How to use Jolteon\n\n1. Create a `.env` file like the `.env.example` one you find in this repository and fill it with your Lightdash database connection parameters.\n\n2. Create a `config.yaml` file like the `config_example.yaml` one you find in this repository. This file should be structured as follows:\n\n    - `old_table` should be filled with the previous name of your dbt model (if you have changed it) or with the current name of it (if you haven't changed it).\n\n    - `new_table` should be filled with the current name of your dbt model only when you have changed it, otherwise it should be left empty.\n\n    - `fields_raw_mapping` should be filled with the mapping of the metrics and the dimensions you have changed. If you haven't changed any metric or dimension, you can also leave it empty.\n\n    - `query_ids` should be filled with the ids of the charts you want to affect when updating the database. If you don't known what are the ids of the charts (and you probably won't the first time), you can run `jolteon get-ids`. You will be presented with a table containing the id, the name and the workspace of all the charts of your Lightdash instance.\n\n3. Run `jolteon update-db config.yaml`.\n",
    'author': 'Alex Ceccotti',
    'author_email': 'alexceccotti5995@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
