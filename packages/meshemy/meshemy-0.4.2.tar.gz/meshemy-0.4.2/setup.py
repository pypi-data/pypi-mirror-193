# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meshemy',
 'meshemy.blender',
 'meshemy.blender.shortcut',
 'meshemy.cookbook',
 'meshemy.utility']

package_data = \
{'': ['*']}

install_requires = \
['numpy<1.24.0',
 'ordered-set>=4.1.0,<5.0.0',
 'pydantic-numpy>=1.3.0,<2.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'pymeshfix>=0.16.2,<0.17.0']

extras_require = \
{'blender': ['bpy>=3.4.0,<4.0.0'],
 'full': ['bpy>=3.4.0,<4.0.0', 'open3d==0.16.0'],
 'open3d': ['open3d==0.16.0']}

setup_kwargs = {
    'name': 'meshemy',
    'version': '0.4.2',
    'description': 'Developer friendly suite for manipulating mesh',
    'long_description': '# Meshemy: Python toolbelt for manipulating mesh\nConsolidation package for manipulating mesh. Comes with cookbook models from each package\n\n## Installation\n```shell\npip install meshemy[full]\n```\nUse it in your poetry package\n```shell\npoetry add meshemy -E full\n```\n\n## Usage\nYou need to pick at least one extra for this package to be useful. Install all modules by installing `full`.\n\n### Cookbook\nCurrently, only Blender and Open3D is supported.\n\n#### Blender\nThe `blender` extra must be installed.\n```python\nfrom meshemy.cookbook.blender import BlenderCookbook\n\nblender_cook = BlenderCookbook.from_file("path_to_mesh.<any_format>")\nblender_cook.planar_decimate(degree_tol=5.0)\n```\nYou can convert to any other cookbook `.to_o3d()`, for instance.\n\n#### Open3D\nThe `open3d` extra must be installed.\n```python\nfrom meshemy.cookbook.open3d import Open3dCookbook\n\nblender_cook = Open3dCookbook.from_file("path_to_mesh.<any_format>")\nblender_cook.smoothen(5)\nblender_cook.repair()\n```\n\n### More\nFor more information, look at the source code, it is relatively easy to read. Start in the `cookbook` submodule.',
    'author': 'caniko',
    'author_email': 'canhtart@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<3.11.0',
}


setup(**setup_kwargs)
