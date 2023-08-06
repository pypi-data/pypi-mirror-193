# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['instainteracts', 'instainteracts.helpers']

package_data = \
{'': ['*']}

install_requires = \
['pyperclip>=1.8.2,<2.0.0',
 'selenium>=4.8.0,<5.0.0',
 'webdriver-manager>=3.8.5,<4.0.0']

setup_kwargs = {
    'name': 'instainteracts',
    'version': '1.0.3',
    'description': 'Instainteracts is an automation tool for Instagram interactions',
    'long_description': "# InstaInteracts\nInstaInteracts is an automation tool for Instagram interactions (follow, like, comment).\n\n## How to install\nYou can install instainteracts by running the following command:\n```\npip install instainteracts\n```\n\n## Basic usage\nThe following example shows how to use InstaInteracts:\n```py\nfrom instainteracts import InstaInteracts\n\nusername = '' # your username\npassword = '' # your password\nhashtag = 'insta' # hashtag to interact with\n\ninsta = InstaInteracts(username, password)\n# for all optional arguments, read the docs below\n\ninsta.comment_by_hashtag(\n    hashtag,\n    ['Comment', u'Emojis supported 🔥'], # list of comments\n    only_recent=True, # interact only with recent posts\n    limit=1 # limit of comments\n)\n\ninsta.follow_by_hashtag(\n    hashtag,\n    limit=2 # limit of follows\n)\n\ninsta.like_by_hashtag(\n    hashtag,\n    limit=3 # limit of likes\n)\n\ninsta.unfollow(5) # will unfollow 5 users\n```\n\n## Docs\nAll InstaInteracts methods are documented at https://instainteracts.pages.dev",
    'author': 'Manuel',
    'author_email': 'hi@manugmg.anonaddy.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
