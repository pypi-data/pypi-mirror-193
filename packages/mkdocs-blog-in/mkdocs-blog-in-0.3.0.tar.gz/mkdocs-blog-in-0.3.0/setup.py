# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mkdocs_blog_in', 'mkdocs_blog_in.cli']

package_data = \
{'': ['*'], 'mkdocs_blog_in': ['lang/*', 'templates/*']}

install_requires = \
['mkdocs>=1.4.2,<2.0.0', 'python-frontmatter>=1.0.0,<2.0.0']

entry_points = \
{'console_scripts': ['mkdocs-blog-in = mkdocs_blog_in.cli.command:app'],
 'mkdocs.plugins': ['blog = mkdocs_blog_in.blog:BlogInPlugin']}

setup_kwargs = {
    'name': 'mkdocs-blog-in',
    'version': '0.3.0',
    'description': 'Blogging plugin for MkDocs',
    'long_description': "# mkdocs-blog-in\n\n[![PyPI version](https://badge.fury.io/py/mkdocs-blog-in.svg)](https://badge.fury.io/py/mkdocs-blog-in)\n\nThis plugin change behaviour of MkDocs, so it allows to use it as a blogging platform.\n\n> **Note**\n> As a base for any development, mkdocs-material theme was used.\n\n> **Warning**\n> Consider this plugin as a beta, so before any use make sure you have a backup of your data.\n\nIf you have found any issue, have an idea for a feature, please submit an issue.\n\n## Features\n\nList of included features (more documentation is needed):\n\n- automatic blog post index page generation with blog post teasers based on delimeter inside a blog post and own template (delimeter can be changed in plugin config in mkdocs.yaml),\n- blog post/page update date based on blog post metadata,\n- separate directory for blog post documents with auto generated separate navigation (blog posts are sorted from newest to oldest)\n- home page set to blog post index with possibility to rename,\n- auto adding link to full blog post from blog post index file (under each post that has teaser delimeter, if delimeter is not present, then full post is inside post index file, but is preserved in blog post navigation and site map).\n- added sub pages for blog posts: archive, categories, tags\n\n## How To\n\n[TODO]\n\n## Todo's\n\nThis list is unordered so functionalities can be added in whenever upcoming version:\n\n- [ ] add cli tool for creating an empty blog post and page\n- [ ] add templates overrides (same mechanism as in mkdocs-material theme) with cli tool to copy a template\n- [ ] add social media preview\n- [ ] add unittests\n- [ ] add page/post meta to publish state like: draft, published, hidden\n- [ ] create documentation\n- [ ] extend categories functionality like: possibility to add multiple categories (like tags), configurable limit of categories (with checks) and configurable list of categories\n- [ ] add configurable date format\n- [ ] image optimization (pngquant and jpeg-quantsmooth + mozjpeg) with cache\n\n## Version history\n\n### 0.3.0\n\n- fix: for wrong directory structure in site-packages after install\n\n### 0.2.0\n\n- added: sub pages for archive, categories, blog\n- added: configurable blog posts pagination with page navigation\n- added: interface language change: EN and PL (help wanted with more languages)\n- added: possibility to override for all interface text elements\n\n### 0.1.0 - initial release\n\n- added: blog post update date based on metadata\n- added: blog post url link based on metadata\n- added: blog post tags and categories based on metadata\n- added: support for blog post teaser\n- added: auto generation of blog posts navigation\n",
    'author': "Maciej 'maQ' Kusz",
    'author_email': 'maciej.kusz@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mkusz/mkdocs-blog-in',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
