# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['judoscale', 'judoscale.core', 'judoscale.django', 'judoscale.flask']

package_data = \
{'': ['*']}

install_requires = \
['requests<3.0.0']

setup_kwargs = {
    'name': 'judoscale-python',
    'version': '0.1.2',
    'description': 'Official Python adapter for Judoscale — the advanced autoscaler for Heroku',
    'long_description': '# `judoscale-python` is now `judoscale` on PyPI\n\nThis package has been renamed. New package: https://pypi.org/project/judoscale/.\n',
    'author': 'Adam McCrea',
    'author_email': 'adam@adamlogic.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/judoscale/judoscale-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
