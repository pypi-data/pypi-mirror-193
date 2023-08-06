# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['ansi2txt']
entry_points = \
{'console_scripts': ['ansi2txt = ansi2txt:main']}

setup_kwargs = {
    'name': 'ansi2txt',
    'version': '0.2.0',
    'description': 'ansi to plain text converter',
    'long_description': "# ansi2txt\n\nansi to plain text converter\n\n## Related\n\nHere are some related projects\n\n- [colorized-logs](https://github.com/kilobyte/colorized-logs)\n- [strip-ansi-cli](https://github.com/chalk/strip-ansi-cli)\n\n## Acknowledgements\n\nThis code base is a translation/port of the `ansi2txt.c` code base from [colorized-logs](https://github.com/kilobyte/colorized-logs) to Python3 and Bash.\nThis project came about because I liked the original `ansi2txt`'s output but did not want to have to compile it or ship binaries around.\nI ported ansi2txt.c → ansi2txt.py but then came across an environment without python so went ansi2txt.py → ansi2txt.sh.\n\n## License\n\n[AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) AND [MIT](https://choosealicense.com/licenses/mit/)\n\n## Running Tests\n\nTo run tests, run the following command\n\n```bash\nbats ansi2txt.bats\n```\n",
    'author': 'Manuel Mendez',
    'author_email': 'git@i.m.mmlb.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
