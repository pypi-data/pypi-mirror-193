# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_unicorn',
 'django_unicorn.components',
 'django_unicorn.management.commands',
 'django_unicorn.templatetags',
 'django_unicorn.views',
 'django_unicorn.views.action_parsers']

package_data = \
{'': ['*'],
 'django_unicorn': ['static/unicorn/js/*',
                    'static/unicorn/js/morphdom/2.6.1/*',
                    'templates/unicorn/*']}

install_requires = \
['beautifulsoup4>=4.8.0',
 'cachetools>=4.1.1,<5.0.0',
 'decorator>=4.4.2,<5.0.0',
 'django>=2.2',
 'orjson>=3.6.0,<4.0.0',
 'shortuuid>=1.0.1,<2.0.0']

extras_require = \
{':python_version < "3.7"': ['dataclasses>=0.8.0,<0.9.0'],
 'docs': ['Sphinx>=4.3.2,<5.0.0',
          'linkify-it-py>=1.0.3,<2.0.0',
          'myst-parser>=0.16.1,<0.17.0',
          'furo>=2021.11.23,<2022.0.0',
          'sphinx-copybutton>=0.4.0,<0.5.0',
          'sphinx-autobuild>=2021.3.14,<2022.0.0',
          'rst2pdf>=0.98,<0.99'],
 'minify': ['htmlmin>=0.1.12,<0.2.0']}

setup_kwargs = {
    'name': 'django-unicorn-gbusby',
    'version': '0.50.3',
    'description': '(Fork)A magical full-stack framework for Django.',
    'long_description': '<p align="center">\n  <a href="https://www.django-unicorn.com/"><img src="https://www.django-unicorn.com/static/img/unicorn.svg" alt="django-unicorn logo" height="80"/></a>\n</p>\n<h1 align="center"><a href="https://www.django-unicorn.com/">Unicorn</a></h1>\n<p align="center">The magical full-stack framework for Django ✨</p>\n\n![PyPI](https://img.shields.io/pypi/v/django-unicorn?color=blue&style=flat-square)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/django-unicorn?color=blue&style=flat-square)\n![GitHub Sponsors](https://img.shields.io/github/sponsors/adamghill?color=blue&style=flat-square)\n\n<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->\n[![All Contributors](https://img.shields.io/badge/all_contributors-17-orange.svg?style=flat-square)](#contributors-)\n<!-- ALL-CONTRIBUTORS-BADGE:END -->\n\n[Unicorn](https://www.django-unicorn.com) is a reactive component framework that progressively enhances a normal Django view, makes AJAX calls in the background, and dynamically updates the DOM. It seamlessly extends Django past its server-side framework roots without giving up all of its niceties or re-building your website.\n\n## ⚡ How to use\n\n1. [Install](https://www.django-unicorn.com/docs/installation/) `Unicorn`\n1. [Create](https://www.django-unicorn.com/docs/components/) a component\n1. Load the `Unicorn` templatetag with `{% load unicorn %}` and add the component to your template with `{% unicorn \'component-name\' %}`\n1. 🎉\n\n## 📖 More details\n\n- [Changelog](https://www.django-unicorn.com/docs/changelog/)\n- [Docs](https://www.django-unicorn.com/docs/)\n- [Screencasts](https://www.django-unicorn.com/screencasts/installation)\n- [Examples](https://www.django-unicorn.com/examples/todo)\n\n## 🔧 To hack on the code\n\n### Python\n\n1. `poetry install -E minify -E docs`\n1. `poetry run pytest`\n\n### JavaScript\n\n1. `npm install`\n1. `npm run test`\n\nCheck out [DEVELOPING.md](DEVELOPING.md) for more details.\n\n## 👏 Contributors\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tbody>\n    <tr>\n      <td align="center" valign="top" width="14.28%"><a href="https://adamghill.com"><img src="https://avatars0.githubusercontent.com/u/317045?v=4?s=100" width="100px;" alt="Adam Hill"/><br /><sub><b>Adam Hill</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=adamghill" title="Code">💻</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=adamghill" title="Tests">⚠️</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://python3.ninja"><img src="https://avatars1.githubusercontent.com/u/44167?v=4?s=100" width="100px;" alt="Andres Vargas"/><br /><sub><b>Andres Vargas</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=zodman" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="http://iskra.ml"><img src="https://avatars3.githubusercontent.com/u/6555851?v=4?s=100" width="100px;" alt="Eddy Ernesto del Valle Pino"/><br /><sub><b>Eddy Ernesto del Valle Pino</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=edelvalle" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/yaser-al-najjar-429b9096/"><img src="https://avatars3.githubusercontent.com/u/10493809?v=4?s=100" width="100px;" alt="Yaser Al-Najjar"/><br /><sub><b>Yaser Al-Najjar</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=yaseralnajjar" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sbidy"><img src="https://avatars.githubusercontent.com/u/1077364?v=4?s=100" width="100px;" alt="Stephan Traub"/><br /><sub><b>Stephan Traub</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=sbidy" title="Tests">⚠️</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/frbor"><img src="https://avatars.githubusercontent.com/u/2320183?v=4?s=100" width="100px;" alt="Fredrik Borg"/><br /><sub><b>Fredrik Borg</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=frbor" title="Code">💻</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=frbor" title="Tests">⚠️</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mbacicc"><img src="https://avatars.githubusercontent.com/u/46646960?v=4?s=100" width="100px;" alt="mbacicc"/><br /><sub><b>mbacicc</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=mbacicc" title="Code">💻</a></td>\n    </tr>\n    <tr>\n      <td align="center" valign="top" width="14.28%"><a href="http://ambient-innovation.com"><img src="https://avatars.githubusercontent.com/u/3176075?v=4?s=100" width="100px;" alt="Ron"/><br /><sub><b>Ron</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=GitRon" title="Documentation">📖</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Franziskhan"><img src="https://avatars.githubusercontent.com/u/86062014?v=4?s=100" width="100px;" alt="Franziskhan"/><br /><sub><b>Franziskhan</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=Franziskhan" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/joshiggins"><img src="https://avatars.githubusercontent.com/u/5124298?v=4?s=100" width="100px;" alt="Josh Higgins"/><br /><sub><b>Josh Higgins</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=joshiggins" title="Tests">⚠️</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=joshiggins" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MayasMess"><img src="https://avatars.githubusercontent.com/u/51958712?v=4?s=100" width="100px;" alt="Amayas Messara"/><br /><sub><b>Amayas Messara</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=MayasMess" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="http://www.apoorvapandey.com"><img src="https://avatars.githubusercontent.com/u/21103831?v=4?s=100" width="100px;" alt="Apoorva Pandey"/><br /><sub><b>Apoorva Pandey</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=apoorvaeternity" title="Tests">⚠️</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=apoorvaeternity" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="http://www.nerdocs.at"><img src="https://avatars.githubusercontent.com/u/2955584?v=4?s=100" width="100px;" alt="Christian González"/><br /><sub><b>Christian González</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=nerdoc" title="Code">💻</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=nerdoc" title="Documentation">📖</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/robwa"><img src="https://avatars.githubusercontent.com/u/4658937?v=4?s=100" width="100px;" alt="robwa"/><br /><sub><b>robwa</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=robwa" title="Code">💻</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=robwa" title="Tests">⚠️</a></td>\n    </tr>\n    <tr>\n      <td align="center" valign="top" width="14.28%"><a href="https://medium.com/@pbadeer"><img src="https://avatars.githubusercontent.com/u/467756?v=4?s=100" width="100px;" alt="Preston Badeer"/><br /><sub><b>Preston Badeer</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=pbadeer" title="Documentation">📖</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/stat1c-void"><img src="https://avatars.githubusercontent.com/u/9142081?v=4?s=100" width="100px;" alt="Sergei"/><br /><sub><b>Sergei</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=stat1c-void" title="Documentation">📖</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=stat1c-void" title="Code">💻</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=stat1c-void" title="Tests">⚠️</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/bazubii"><img src="https://avatars.githubusercontent.com/u/12039914?v=4?s=100" width="100px;" alt="bazubii"/><br /><sub><b>bazubii</b></sub></a><br /><a href="https://github.com/adamghill/django-unicorn/commits?author=bazubii" title="Code">💻</a> <a href="https://github.com/adamghill/django-unicorn/commits?author=bazubii" title="Tests">⚠️</a></td>\n    </tr>\n  </tbody>\n</table>\n\n<!-- markdownlint-restore -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n',
    'author': 'Adam Hill',
    'author_email': 'unicorn@adamghill.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.django-unicorn.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
