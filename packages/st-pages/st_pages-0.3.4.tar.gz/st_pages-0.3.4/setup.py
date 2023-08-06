# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['st_pages']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.4,<2.0.0', 'streamlit>=1.10.0']

setup_kwargs = {
    'name': 'st-pages',
    'version': '0.3.4',
    'description': 'An experimental version of Streamlit Multi-Page Apps',
    'long_description': '# Streamlit-Pages\n\n[![Releases](https://img.shields.io/pypi/v/st-pages)](https://pypi.org/project/st-pages/)\n[![Build Status](https://img.shields.io/github/actions/workflow/status/blackary/st_pages/testing.yml?branch=main)](https://github.com/blackary/st_pages/actions?query=workflow%3A%22testing%22+branch%3Amain)\n![Python Versions](https://img.shields.io/pypi/pyversions/st_pages.svg)\n![Streamlit versions](https://img.shields.io/badge/streamlit-1.15.0--1.18.0-white.svg)\n![License](https://img.shields.io/github/license/blackary/st_pages)\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://st-pages.streamlit.app)\n\nAuthor: [@blackary](https://github.com/blackary)\n\nCode: https://github.com/blackary/st_pages\n\n## Installation\n\n```sh\npip install st-pages\n```\n\n## See it in action\n\nBasic example: https://st-pages.streamlit.app/\n\nExample with sections: https://st-pages-sections.streamlit.app/\n\n## Why st-pages?\n\n> Summary: st-pages allows you to set the page names, order, and icons (and optionally\n> group the pages into sections) in a multipage Streamlit app from your code without\n> having to rename the files.\n\n![image](https://user-images.githubusercontent.com/4040678/204576356-a436713f-93e4-41e3-82b9-6efeff744355.png)\n\nStreamlit has native support for [multi-page apps](https://blog.streamlit.io/introducing-multipage-apps/)\nwhere page filenames are the source of truth for page settings. But, it\'s a bit annoying\nto have to change the filename to change the names in the sidebar or reorder the pages\nin your app. Even more, I really dislike having to put emojis in filenames.\n\nThis is an experimental package to try out how page-management might work if\nyou could name the pages whatever you wanted, and could manage which pages are visible,\nand how they appear in the sidebar, via a setup function.\n\nThis enables you to set page _name_, _icon_ and _order_ independently of file name/path,\nwhile still retaining the same sidebar & url behavior of current streamlit multi-page\napps.\n\n## How to use\n\n### Method one: declare pages inside your streamlit code\n\n```python\nfrom st_pages import Page, show_pages, add_page_title\n\n# Optional -- adds the title and icon to the current page\nadd_page_title()\n\n# Specify what pages should be shown in the sidebar, and what their titles and icons\n# should be\nshow_pages(\n    [\n        Page("streamlit_app.py", "Home", "🏠"),\n        Page("other_pages/page2.py", "Page 2", ":books:"),\n    ]\n)\n```\n\nIf you want to organize your pages into sections with indention showing which pages\nbelong to which section, you can do the following:\n\n```python\nfrom st_pages import Page, Section, show_pages, add_page_title\n\nadd_page_title() # By default this also adds indentation\n\n# Specify what pages should be shown in the sidebar, and what their titles and icons\n# should be\nshow_pages(\n    [\n        Page("streamlit_app.py", "Home", "🏠"),\n        Page("other_pages/page2.py", "Page 2", ":books:"),\n        Section("My section", icon="🎈️"),\n        # Pages after a section will be indented\n        Page("Another page", icon="💪"),\n    ]\n)\n```\n\n### Method two: declare pages inside of a config file\n\nContents of `.streamlit/pages.toml`\n\n```toml\n[[pages]]\npath = "streamlit_app.py"\nname = "Home"\nicon = "🏠"\n\n[[pages]]\npath = "other_pages/page2.py"\nname = "Page 2"\nicon = ":books:"\n```\n\nExample with sections:\n\n```toml\n[[pages]]\npath = "streamlit_app.py"\nname = "Home"\nicon = "🏠"\n\n[[pages]]\npath = "other_pages/page2.py"\nname = "Page 2"\nicon = ":books:"\n\n[[pages]]\nname = "My second"\nicon = "🎈️"\nis_section = true\n\n# Pages after an `is_section = true` will be indented\n[[pages]]\nname = "Another page"\nicon = "💪"\n```\n\nStreamlit code:\n\n```python\nfrom st_pages import show_pages_from_config, add_page_title\n\n# Either this or add_indentation() MUST be called on each page in your\n# app to add indendation in the sidebar\nadd_page_title()\n\nshow_pages_from_config()\n```\n',
    'author': 'Zachary Blackwood',
    'author_email': 'zachary@streamlit.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
}


setup(**setup_kwargs)
