# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gyver', 'gyver.attrs', 'gyver.attrs.converters', 'gyver.attrs.utils']

package_data = \
{'': ['*']}

install_requires = \
['gyver-attrs-converter>=0.4.0,<0.5.0',
 'orjson>=3.8.6,<4.0.0',
 'typing-extensions>=4.5.0,<5.0.0']

setup_kwargs = {
    'name': 'gyver-attrs',
    'version': '0.1.2',
    'description': '',
    'long_description': '# Gyver Attrs\n===========\n\nGyver Attrs is a lightweight library that simplifies the creation of Python data classes by providing a single decorator function, `define()`, that automatically adds useful class methods and attributes. With Gyver Attrs, you can easily create data classes that are immutable, hashable, comparable, and optimized for memory usage. Gyver Attrs will also support your descriptors that have private_names in slotted and frozen classes.\n\nFeatures\n--------\nThe `define()` function adds the following features to data classes:\n\n* `__init__()` method for class initialization\n* `__repr__()` method for string representation of the class instance\n* `__eq__()` method for equality comparison of class instances\n* `__ne__()` method for inequality comparison of class instances\n* rich comparison methods (i.e., `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`) for comparing class instances\n* `__hash__()` method for hashable class instances\n* `__slots__`attribute for reducing the memory footprint of class instances\n* Fast converters to transform objects to and from dictionaries and JSON formats. These converters are implemented using a custom conversion library written in Rust and the ORJSON package. The conversion library is provided to offer high performance, making it suitable for large scale data operations.\n\nTo use the converters, the following functions are provided:\n\n* **`asdict(obj)`**: Returns a dictionary containing the attributes of the input object.\n* **`from_dict(type, dict)`**: Creates a new object of the specified type from the given dictionary.\n* **`asjson(obj)`**: Returns a JSON string containing the attributes of the input object.\n* **`from_json(type, obj)`**: Creates a new object of the specified type from the given JSON string.\n\n\nGyver Attrs uses the function `gyver.attrs.info` and the class `gyver.attrs.FieldInfo` in the same way as you would use `dataclass.field` or `pydantic.Field`. It accepts the following parameters:\n\n* default: the default value for the field.\n* alias: an alias name for the field.\n* kw_only: whether the field is keyword-only.\n* eq: whether the field should be included in the equality comparison method or a callable function for customizing equality comparison.\n* order: whether the field should be included in the rich comparison methods or a callable function for customizing rich comparison.\n\nThe info() function returns a new instance of FieldInfo based on the parameters passed in. It accepts the same parameters as FieldInfo. FieldInfo provides additional methods like asdict() to get a dictionary representation of the field information, duplicate() to create a copy of the field with any overrides passed in, and build() to create a Field object based on the field information.\n\nUsage\n-----\nThe `define()` function can be used as a decorator on a data class definition or on an existing data class. It accepts the following keyword arguments:\n\n* `frozen`: whether to create an immutable class or not (default is `True`)\n* `kw_only`: whether to include keyword-only parameters in the constructor or not (default is `False`)\n* `slots`: whether to generate a class using `__slots__` or not (default is `True`)\n* `repr`: whether to generate a `__repr__` method or not (default is `True`)\n* `eq`: whether to generate an `__eq__` method or not (default is `True`)\n* `order`: whether to generate rich comparison methods or not (default is `True`)\n* `hash`: whether to generate a `__hash__` method or not (default is `None`)\n\nUsage Examples\n--------\nHere\'s an example of how to use the `define()` function:\n\n```python\nfrom gyver_attrs import define\n\n@define\nclass MyClass:\n    x: int\n    y: int\n\n@define(frozen=True, hash=True)\nclass Person:\n    name: str\n    age: int\n\np1 = Person(name="Alice", age=25)\np2 = Person(name="Bob", age=30)\np3 = Person(name="Alice", age=25)\n\nassert p1 != p2\nassert p1 == p3\nassert hash(p1) == hash(p3)\n\n@define\nclass Rectangle:\n    width: float\n    height: float\n\n    def area(self) -> float:\n        return self.width * self.height\n\n    def perimeter(self) -> float:\n        return 2 * (self.width + self.height)\n\nr = Rectangle(width=10.0, height=5.0)\n\nassert r.area() == 50.0\nassert r.perimeter() == 30.0\n\n\n@define(order=False)\nclass Point:\n    x: int\n    y: int\n\n    def __add__(self, other: \'Point\') -> \'Point\':\n        return Point(self.x + other.x, self.y + other.y)\n\n    def __sub__(self, other: \'Point\') -> \'Point\':\n        return Point(self.x - other.x, self.y - other.y)\n\np1 = Point(x=1, y=2)\np2 = Point(x=3, y=4)\n\nassert p1 + p2 == Point(x=4, y=6)\nassert p2 - p1 == Point(x=2, y=2)\n```\n\nInstallation\n--------\nYou can install gyver-attrs using pip\n```console\npip install gyver-attrs\n```\n\nContributing\n--------\nContributions are welcome! Here are the steps to get started:\n* Fork the repository and clone it locally.\n* Install the required dependencies with **`poetry install --all-extras`**.\n* Create a new branch for your changes with **`git checkout -b my-branch`**.\n* Make your desired changes.\n* Ensure that all tests pass with **`make test`**.\n* Format the code with **`make format`**.\n* Push your changes to your fork and create a pull request.\n\nThank you for contributing to gyver-attrs!',
    'author': 'Gustavo Cardoso',
    'author_email': 'self.gustavocorrea@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
