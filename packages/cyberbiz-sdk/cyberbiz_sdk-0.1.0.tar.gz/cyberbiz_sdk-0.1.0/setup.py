# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cyberbiz_sdk']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'cyberbiz-sdk',
    'version': '0.1.0',
    'description': 'An unofficial python sdk for cyberbiz',
    'long_description': '# Testing\n```bash\npoetry run pytest\n```\n\n\n# Document Ref:\nDocument: https://www.cyberbiz.io/support/?p=20739\nPlayground: https://api-doc.cyberbiz.co/v1/api_document\n\n# package\nhttps://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
