# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sunpeek_exampledata']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sunpeek-exampledata',
    'version': '0.1.0.dev1',
    'description': 'Sample data for demonstration of the sunpeek solar thermal performance assessment tool',
    'long_description': '# SunPeek Demonstration Package\nThis package contains sample data for demonstrating the features of the [SunPeek](https://pypi.org/project/sunpeek/) \nsolar thermal performance assessment package. To install this package with sunpeek, run `pip install sunpeek[demo]`\n\n<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This package is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.',
    'author': 'Philip Ohnewein, Daniel Tschopp, Lukas Feierl, Marnoch Hamilton-Jones',
    'author_email': 'None',
    'maintainer': 'Philip Ohnewein',
    'maintainer_email': 'p.ohnewein@aee.at',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
