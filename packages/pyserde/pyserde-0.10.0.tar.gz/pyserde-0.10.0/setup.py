# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['serde']

package_data = \
{'': ['*']}

install_requires = \
['casefy', 'jinja2', 'typing_inspect>=0.4.0']

extras_require = \
{':python_version ~= "3.7.0"': ['typing_extensions>=4.1.0'],
 'all': ['msgpack', 'tomli', 'tomli-w', 'pyyaml', 'orjson'],
 'all:python_version ~= "3.10"': ['numpy>1.22.0',
                                  'numpy>1.22.0',
                                  'numpy>1.22.0',
                                  'numpy>1.22.0'],
 'all:python_version ~= "3.7.0"': ['numpy>1.21.0',
                                   'numpy>1.21.0',
                                   'numpy>1.21.0',
                                   'numpy>1.21.0'],
 'all:python_version ~= "3.8.0"': ['numpy>1.21.0',
                                   'numpy>1.21.0',
                                   'numpy>1.21.0',
                                   'numpy>1.21.0'],
 'all:python_version ~= "3.9.0"': ['numpy>1.21.0',
                                   'numpy>1.21.0',
                                   'numpy>1.21.0',
                                   'numpy>1.21.0'],
 'msgpack': ['msgpack'],
 'numpy:python_version ~= "3.10"': ['numpy>1.22.0',
                                    'numpy>1.22.0',
                                    'numpy>1.22.0',
                                    'numpy>1.22.0'],
 'numpy:python_version ~= "3.7.0"': ['numpy>1.21.0',
                                     'numpy>1.21.0',
                                     'numpy>1.21.0',
                                     'numpy>1.21.0'],
 'numpy:python_version ~= "3.8.0"': ['numpy>1.21.0',
                                     'numpy>1.21.0',
                                     'numpy>1.21.0',
                                     'numpy>1.21.0'],
 'numpy:python_version ~= "3.9.0"': ['numpy>1.21.0',
                                     'numpy>1.21.0',
                                     'numpy>1.21.0',
                                     'numpy>1.21.0'],
 'orjson': ['orjson'],
 'toml': ['tomli', 'tomli-w'],
 'yaml': ['pyyaml']}

setup_kwargs = {
    'name': 'pyserde',
    'version': '0.10.0',
    'description': 'Yet another serialization library on top of dataclasses',
    'long_description': '# `pyserde`\n\nYet another serialization library on top of [dataclasses](https://docs.python.org/3/library/dataclasses.html), inspired by [serde-rs](https://github.com/serde-rs/serde).\n\n[![image](https://img.shields.io/pypi/v/pyserde.svg)](https://pypi.org/project/pyserde/)\n[![image](https://img.shields.io/pypi/pyversions/pyserde.svg)](https://pypi.org/project/pyserde/)\n![Tests](https://github.com/yukinarit/pyserde/workflows/Tests/badge.svg)\n[![codecov](https://codecov.io/gh/yukinarit/pyserde/branch/main/graph/badge.svg)](https://codecov.io/gh/yukinarit/pyserde)\n\n[Guide](https://yukinarit.github.io/pyserde/guide) | [API Docs](https://yukinarit.github.io/pyserde/api/serde.html) | [Examples](./examples)\n\n## Overview\n\nDeclare a class with pyserde\'s `@serde` decorator.\n\n```python\n@serde\n@dataclass\nclass Foo:\n    i: int\n    s: str\n    f: float\n    b: bool\n```\n\nYou can serialize `Foo` object into JSON.\n\n```python\n>>> to_json(Foo(i=10, s=\'foo\', f=100.0, b=True))\n\'{"i":10,"s":"foo","f":100.0,"b":true}\'\n```\n\nYou can deserialize JSON into `Foo` object.\n```python\n>>> from_json(Foo, \'{"i": 10, "s": "foo", "f": 100.0, "b": true}\')\nFoo(i=10, s=\'foo\', f=100.0, b=True)\n```\n\n## Features\n\n- Supported data formats\n    - dict\n    - tuple\n    - JSON\n\t- Yaml\n\t- Toml\n\t- MsgPack\n    - Pickle\n- Supported types\n    - Primitives (`int`, `float`, `str`, `bool`)\n    - Containers\n        - `List`, `Set`, `Tuple`, `Dict`\n        - [`FrozenSet`](https://docs.python.org/3/library/stdtypes.html#frozenset), [`DefaultDict`](https://docs.python.org/3/library/collections.html#collections.defaultdict)\n    - [`typing.Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)\n    - [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union)\n    - User defined class with [`@dataclass`](https://docs.python.org/3/library/dataclasses.html)\n    - [`typing.NewType`](https://docs.python.org/3/library/typing.html#newtype) for primitive types\n    - [`typing.Any`](https://docs.python.org/3/library/typing.html#the-any-type)\n    - [`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal)\n    - [`typing.Generic`](https://docs.python.org/3/library/typing.html#user-defined-generic-types)\n    - [`typing.ClassVar`](https://docs.python.org/3/library/typing.html#user-defined-generic-type://docs.python.org/3/library/typing.html#typing.ClassVar)\n    - [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum) and [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum)\n    - Standard library\n        - [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html)\n        - [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html)\n        - [`uuid.UUID`](https://docs.python.org/3/library/uuid.html)\n        - [`datetime.date`](https://docs.python.org/3/library/datetime.html#date-objects), [`datetime.time`](https://docs.python.org/3/library/datetime.html#time-objects), [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects)\n        - [`ipaddress`](https://docs.python.org/3/library/ipaddress.html)\n    - PyPI library\n        - [`numpy`](https://github.com/numpy/numpy) types\n- [Attributes](docs/features/attributes.md)\n- [Decorators](docs/features/decorators.md)\n- [TypeCheck](docs/features/type-check.md)\n- [Union Representation](docs/features/union.md)\n- [Python 3.10 Union operator](docs/features/union-operator.md)\n- [Python 3.9 type hinting](docs/features/python3.9-type-hinting.md)\n- [Postponed evaluation of type annotation](docs/features/postponed-evaluation-of-type-annotation.md)\n- [Forward reference](docs/features/forward-reference.md)\n- [Case Conversion](docs/features/case-conversion.md)\n- [Rename](docs/features/rename.md)\n- [Alias](docs/features/alias.md)\n- [Skip](docs/features/skip.md)\n- [Conditional Skip](docs/features/conditional-skip.md)\n- [Custom field (de)serializer](docs/features/custom-field-serializer.md)\n- [Custom class (de)serializer](docs/features/custom-class-serializer.md)\n- [Flatten](docs/features/flatten.md)\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tbody>\n    <tr>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yukinarit"><img src="https://avatars.githubusercontent.com/u/2347533?v=4?s=60" width="60px;" alt="yukinarit"/><br /><sub><b>yukinarit</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=yukinarit" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/alexmisk"><img src="https://avatars.githubusercontent.com/u/4103218?v=4?s=60" width="60px;" alt="Alexander Miskaryan"/><br /><sub><b>Alexander Miskaryan</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=alexmisk" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ydylla"><img src="https://avatars.githubusercontent.com/u/17772145?v=4?s=60" width="60px;" alt="ydylla"/><br /><sub><b>ydylla</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=ydylla" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kmsquire"><img src="https://avatars.githubusercontent.com/u/223250?v=4?s=60" width="60px;" alt="Kevin Squire"/><br /><sub><b>Kevin Squire</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=kmsquire" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="http://yushiomote.org/"><img src="https://avatars.githubusercontent.com/u/3733915?v=4?s=60" width="60px;" alt="Yushi OMOTE"/><br /><sub><b>Yushi OMOTE</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=YushiOMOTE" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://kngwyu.github.io/"><img src="https://avatars.githubusercontent.com/u/16046705?v=4?s=60" width="60px;" alt="Yuji Kanagawa"/><br /><sub><b>Yuji Kanagawa</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=kngwyu" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://kigawas.me/"><img src="https://avatars.githubusercontent.com/u/4182346?v=4?s=60" width="60px;" alt="Weiliang Li"/><br /><sub><b>Weiliang Li</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=kigawas" title="Code">💻</a></td>\n    </tr>\n    <tr>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mauvealerts"><img src="https://avatars.githubusercontent.com/u/51870303?v=4?s=60" width="60px;" alt="Mauve"/><br /><sub><b>Mauve</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=mauvealerts" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/adsharma"><img src="https://avatars.githubusercontent.com/u/658691?v=4?s=60" width="60px;" alt="adsharma"/><br /><sub><b>adsharma</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=adsharma" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/chagui"><img src="https://avatars.githubusercontent.com/u/1234128?v=4?s=60" width="60px;" alt="Guilhem C."/><br /><sub><b>Guilhem C.</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=chagui" title="Documentation">📖</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tardyp"><img src="https://avatars.githubusercontent.com/u/109859?v=4?s=60" width="60px;" alt="Pierre Tardy"/><br /><sub><b>Pierre Tardy</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=tardyp" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://blog.rnstlr.ch/"><img src="https://avatars.githubusercontent.com/u/1435346?v=4?s=60" width="60px;" alt="Raphael Nestler"/><br /><sub><b>Raphael Nestler</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=rnestler" title="Documentation">📖</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://pranavvp10.github.io/"><img src="https://avatars.githubusercontent.com/u/52486224?v=4?s=60" width="60px;" alt="Pranav V P"/><br /><sub><b>Pranav V P</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=pranavvp10" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://andreymal.org/"><img src="https://avatars.githubusercontent.com/u/3236464?v=4?s=60" width="60px;" alt="andreymal"/><br /><sub><b>andreymal</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=andreymal" title="Code">💻</a></td>\n    </tr>\n    <tr>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jfuechsl"><img src="https://avatars.githubusercontent.com/u/1097068?v=4?s=60" width="60px;" alt="Johann Fuechsl"/><br /><sub><b>Johann Fuechsl</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=jfuechsl" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://github.com/DoeringChristian"><img src="https://avatars.githubusercontent.com/u/23581448?v=4?s=60" width="60px;" alt="DoeringChristian"/><br /><sub><b>DoeringChristian</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=DoeringChristian" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="http://stuart.axelbrooke.com/"><img src="https://avatars.githubusercontent.com/u/2815794?v=4?s=60" width="60px;" alt="Stuart Axelbrooke"/><br /><sub><b>Stuart Axelbrooke</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=soaxelbrooke" title="Code">💻</a></td>\n      <td align="center" valign="top" width="14.28%"><a href="https://kobzol.github.io/"><img src="https://avatars.githubusercontent.com/u/4539057?v=4?s=60" width="60px;" alt="Jakub Beránek"/><br /><sub><b>Jakub Beránek</b></sub></a><br /><a href="https://github.com/yukinarit/pyserde/commits?author=Kobzol" title="Code">💻</a></td>\n    </tr>\n  </tbody>\n  <tfoot>\n    <tr>\n      <td align="center" size="13px" colspan="7">\n        <img src="https://raw.githubusercontent.com/all-contributors/all-contributors-cli/1b8533af435da9854653492b1327a23a4dbd0a10/assets/logo-small.svg">\n          <a href="https://all-contributors.js.org/docs/en/bot/usage">Add your contributions</a>\n        </img>\n      </td>\n    </tr>\n  </tfoot>\n</table>\n\n<!-- markdownlint-restore -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n\n## LICENSE\n\nThis project is licensed under the [MIT license](https://github.com/yukinarit/pyserde/blob/main/LICENSE).\n',
    'author': 'yukinarit',
    'author_email': 'yukinarit84@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/yukinarit/pyserde',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
