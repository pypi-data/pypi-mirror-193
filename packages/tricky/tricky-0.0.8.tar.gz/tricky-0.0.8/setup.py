# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tricky', 'tricky.pydantic', 'tricky.utils']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.5.0']

extras_require = \
{'pydantic': ['pydantic==1.10.4']}

setup_kwargs = {
    'name': 'tricky',
    'version': '0.0.8',
    'description': 'A set of useful features to make working with your code easier.',
    'long_description': '# tricky - that\'s about python.\n\nThis module is simply a collection of useful code, utilities, and functions to simplify your work with the language and the tasks you solve.\n\n## Collection:\n1. Iterables module `tricky.iterables`\n2. Typing `tricky.typing` (wip)\n\n\n## Examples:\n\n### Iterables\n1. Example of **iterables.filter_item**\n ```python\n from tricky.iterables import filter_item\n \n numbers = range(1000)\n result: int = filter_item(\n     numbers,  # the iterable\n     lambda number: number == 342,  # condition to get your item\n     None,  # the default value to return, if condition not met\n )\n print(result)\n # 342\n ```\n\n### Typing\n\n1. An example of a simple use of a **TypedList**:\n```python\nfrom tricky.typing import TypedList\n\nnumbers = TypedList[int](1, 2, 3, 4, 5)\nassert isinstance(numbers, (list, TypedList))  # True\n```\n\nBut if an element with a different type is passed to the list, an exception will be thrown:\n```python\nfrom tricky.typing import TypedList\n\nnumbers = TypedList[int](1, 2, 3, \'string\', 5)\n# ValueError: Passed item "string" of sequence has type <class \'str\'>, but annotated type is <class \'int\'>\n```\n\n2. An example of a simple use of a **AnnotatedString**\n```python\nfrom tricky.typing import AnnotatedString\n\nexpecting_value = \'example\'\nannotated_string = AnnotatedString[\'example\'](expecting_value)\nassert isinstance(AnnotatedString[\'example\'](expecting_value), (str, AnnotatedString))\n```\nBut if the annotated value does not match the one passed, an exception will be thrown\n```python\nfrom tricky.typing import AnnotatedString\n\nbad_value = \'bad_value\'\nannotated_string = AnnotatedString[\'example\'](bad_value)\n# ValueError: Annotated and passed values are not equal \'bad_value\' != \'example\'\n```\n',
    'author': 'Alexander Walther',
    'author_email': 'alexander.walther.engineering@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Walther-s-Engineering/tricky',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
