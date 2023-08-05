# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbt_models_explorer']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['dbt-models-explorer = dbt_models_explorer.__main__:main']}

setup_kwargs = {
    'name': 'dbt-models-explorer',
    'version': '0.1.0',
    'description': 'DBT models explorer with output generator to check, analyze and document',
    'long_description': '# dbt-models-explorer\n\nDBT models explorer with output generator to check, analyze and document\n\n## Features\n\n- Read DBT Models Yml to objectcts and make relationships Analysis\n- Rich Console Output\n- Export to CSV Format\n\n## Run Locally\n\nClone the project\n\n```bash\n  git clone https://github.com/catapimbas/dbt-models-explorer.git\n```\n\nGo to the project directory\n\n```bash\n  cd dbt-models-explorer\n```\n\nInstall dependencies\n\n```bash\n  poetry install\n```\n\nRun\n\n```bash\n  poetry run dbt-models-explorer [<path-to-yml-models> <options>]\n```\n\n## Usage/Examples\n\n### Rich outupt, default\n\n```bash\npoetry run dbt-models-explorer <path-to-yml-models>\n```\n\n### CSV outupt\n\n```bash\npoetry run dbt-models-explorer <path-to-yml-models> --format csv <filename>\n```\n',
    'author': 'Rodrigo Cristiano',
    'author_email': 'rcristianofv@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/catapimbas/dbt-models-explorer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
