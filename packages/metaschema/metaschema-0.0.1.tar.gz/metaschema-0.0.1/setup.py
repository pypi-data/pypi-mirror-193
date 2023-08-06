# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['metaschema']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.5,<2.0.0']

setup_kwargs = {
    'name': 'metaschema',
    'version': '0.0.1',
    'description': 'Repository of Pydantic models for metadata schema.',
    'long_description': '# metaschema\nRepository of Pydantic models for metadata schema.\n',
    'author': 'Aivin V. Solatorio',
    'author_email': 'avsolatorio@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
