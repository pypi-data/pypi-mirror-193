# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rslsync', 'rslsync.commands']

package_data = \
{'': ['*']}

install_requires = \
['urllib3>=1.0']

setup_kwargs = {
    'name': 'rslsync',
    'version': '0.1.1',
    'description': 'A Python client of unofficial Resilio Sync API',
    'long_description': 'A Python client of unofficial Resilio Sync API.\n\n## Usage\n\n```\n\n$ from rslsync import RslClient\n$ c = RslClient("http://localhost:8888/", "user", "pass")\n$ c.folder.list_shared_folders()  # list all shared folders\n$ c.file.list_shared_files()  # list all shared files\n$ share_id = c.file.share_file(path, days)   # share a single file\n$ c.file.create_link(share_id)   # create a share link\n$ c.file.unshare_file(share_id)   # unshare a file\n\n```\n',
    'author': 'Zhongke Chen',
    'author_email': 'github@ch3n2k.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/zhongkechen/python-resilio-sync-unofficial',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
