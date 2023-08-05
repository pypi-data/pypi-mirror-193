# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exitcode']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'exitcode',
    'version': '0.1.0',
    'description': 'Preferred system exit codes as defined by sysexits.h',
    'long_description': '# exitcode\n\nPreferred system exit codes as defined by [`sysexits.h`](https://man.openbsd.org/sysexits).\nThis library is inspired by this [rust library](https://docs.rs/exitcode).\n\n## Example\n\nAll constants from the manpage [sysexits(3)](https://man.openbsd.org/sysexits) are available without the `EX_` prefix.\n\n``` python\nimport exitcode\nimport sys\n\nsys.exit(exitcode.OK)\n```',
    'author': 'Stefan Tatschner',
    'author_email': 'stefan@rumpelsepp.org',
    'maintainer': 'Stefan Tatschner',
    'maintainer_email': 'stefan@rumpelsepp.org',
    'url': 'https://github.com/rumpelsepp/exitcode',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
