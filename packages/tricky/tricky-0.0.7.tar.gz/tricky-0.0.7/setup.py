# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tricky', 'tricky.pydantic', 'tricky.utils']

package_data = \
{'': ['*']}

extras_require = \
{'pydantic': ['pydantic==1.10.4']}

setup_kwargs = {
    'name': 'tricky',
    'version': '0.0.7',
    'description': 'A set of useful features to make working with your code easier.',
    'long_description': "# tricky - that's about python.\n\nThis module is simply a collection of useful code, utilities, and functions to simplify your work with the language and the tasks you solve.\n\n## Collection:\n1. Iterables module `tricky.iterables`\n2. Typing `tricky.typing` (wip)\n\n\n## Examples:\n\n1. Example of **iterables.filter_item**\n    ```python\n    from tricky.iterables import filter_item\n    \n    numbers = range(1000)\n    result: int = filter_item(\n        numbers,  # the iterable\n        lambda number: number == 342,  # condition to get your item\n        None,  # the default value to return, if condition not met\n    )\n    print(result)\n    # 342\n    ```\n\n2. Example of **typing**\n    ```python\n    from tricky.typing import TypedList\n    \n    numbers = TypedList[int]([1, 2, 3, 4, 5])\n    assert isinstance(numbers, list)  # True\n    ```\n",
    'author': 'Alexander Walther',
    'author_email': 'alexander.walther.engineering@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Walther-s-Engineering/tricky',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
