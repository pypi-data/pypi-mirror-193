# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wagtail_sb_admin_interface',
 'wagtail_sb_admin_interface.migrations',
 'wagtail_sb_admin_interface.templatetags']

package_data = \
{'': ['*'], 'wagtail_sb_admin_interface': ['templates/wagtailadmin/*']}

install_requires = \
['django-colorfield<1.0.0', 'django<5.0', 'wagtail<5.0']

setup_kwargs = {
    'name': 'wagtail-sb-admin-interface',
    'version': '0.3.0',
    'description': 'Social Networks settings for wagtail sites.',
    'long_description': '![Community-Project](https://gitlab.com/softbutterfly/open-source/open-source-office/-/raw/master/banners/softbutterfly-open-source--banner--community-project.png)\n\n![PyPI - Supported versions](https://img.shields.io/pypi/pyversions/wagtail-sb-admin-interface)\n![PyPI - Package version](https://img.shields.io/pypi/v/wagtail-sb-admin-interface)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/wagtail-sb-admin-interface)\n![PyPI - MIT License](https://img.shields.io/pypi/l/wagtail-sb-admin-interface)\n\n[![Build Status](https://www.travis-ci.org/softbutterfly/wagtail-sb-admin-interface.svg?branch=develop)](https://www.travis-ci.org/softbutterfly/wagtail-sb-admin-interface)\n[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e35e7095857b416696eb58a4ed5d9a15)](https://www.codacy.com/gh/softbutterfly/wagtail-sb-admin-interface/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=softbutterfly/wagtail-sb-admin-interface&amp;utm_campaign=Badge_Grade)\n[![Codacy Badge Coverage](https://app.codacy.com/project/badge/Coverage/e35e7095857b416696eb58a4ed5d9a15)](https://www.codacy.com/gh/softbutterfly/wagtail-sb-admin-interface/dashboard?utm_source=github.com&utm_medium=referral&utm_content=softbutterfly/wagtail-sb-admin-interface&utm_campaign=Badge_Coverage)\n[![codecov](https://codecov.io/gh/softbutterfly/wagtail-sb-admin-interface/branch/master/graph/badge.svg?token=pbqXUUOu1F)](https://codecov.io/gh/softbutterfly/wagtail-sb-admin-interface)\n\n# Wagtail Admin Interface\n\nCustomize the Wagtail admin interface from the admin itself.\n\nInspired by [django-admin-interface](https://github.com/fabiocaccamo/django-admin-interface).\n\n## Requirements\n\n- Python 3.8.1 or higher\n- Django 4.0.0 or higher\n- Wagtail 4.0.0 or higher\n\n## Install\n\n```bash\npip install wagtail-sb-admin-interface\n```\n\n## Usage\n\nAdd `wagtail.contrib.settings`, `wagtail.contrib.modeladmin`, `colorfield` and `wagtail_sb_admin_interface` to your `INSTALLED_APPS` settings\n\n```\nINSTALLED_APPS = [\n  "wagtail_sb_admin_interface",\n  # ...\n  "wagtail.contrib.settings",\n  "wagtail.contrib.modeladmin",\n  "colorfield",\n  # ...\n]\n```\n\n## Docs\n\n- [Ejemplos](https://github.com/softbutterfly/wagtail-sb-admin-interface/wiki)\n- [Wiki](https://github.com/softbutterfly/wagtail-sb-admin-interface/wiki)\n\n## Changelog\n\nAll changes to versions of this library are listed in the [change history](CHANGELOG.md).\n\n## Development\n\nCheck out our [contribution guide](CONTRIBUTING.md).\n\n## Contributors\n\nSee the list of contributors [here](https://github.com/softbutterfly/wagtail-sb-admin-interface/graphs/contributors).\n',
    'author': 'SoftButterfly Development Team',
    'author_email': 'dev@softbutterfly.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/softbutterfly/wagtail-sb-admin-interface',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
