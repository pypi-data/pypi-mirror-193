# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smx', 'test']

package_data = \
{'': ['*'],
 'smx': ['include/*',
         'spcomp/spcomp.elf',
         'spcomp/spcomp.elf',
         'spcomp/spcomp.elf',
         'spcomp/spcomp.elf',
         'spcomp/spcomp.elf',
         'spcomp/spcomp.elf64',
         'spcomp/spcomp.elf64',
         'spcomp/spcomp.elf64',
         'spcomp/spcomp.elf64',
         'spcomp/spcomp.elf64',
         'spcomp/spcomp.exe',
         'spcomp/spcomp.exe',
         'spcomp/spcomp.exe',
         'spcomp/spcomp.exe',
         'spcomp/spcomp.exe',
         'spcomp/spcomp.exe64',
         'spcomp/spcomp.exe64',
         'spcomp/spcomp.exe64',
         'spcomp/spcomp.exe64',
         'spcomp/spcomp.exe64',
         'spcomp/spcomp.macho',
         'spcomp/spcomp.macho',
         'spcomp/spcomp.macho',
         'spcomp/spcomp.macho',
         'spcomp/spcomp.macho']}

install_requires = \
['construct-typing>=0.5.5,<0.6.0', 'construct>=2.10.68,<3.0.0']

setup_kwargs = {
    'name': 'pysmx',
    'version': '0.2.0',
    'description': 'Interact with SourceMod plug-ins',
    'long_description': '# pysmx\n\n**pysmx** is a Python package for parsing, executing, and simulating the environment of SourceMod plug-ins.\n\n\n## Quickstart\n\n```shell\npip install pysmx\n```\n\n```python\nfrom smx.compiler import compile\n\nplugin = compile(\'\'\'\n    public TwoPlusTwo() {\n        return 2 + 2;\n    }\n    public String:Snakes() {\n        new String:s[] = "hiss";\n        return s;\n    }\n\'\'\')\n\nprint(plugin.runtime.call_function_by_name(\'TwoPlusTwo\'))\n# 4\nprint(plugin.runtime.call_function_by_name(\'Snakes\'))\n# \'hiss\'\n```\n',
    'author': 'Zach Kanzler',
    'author_email': 'they4kman@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
