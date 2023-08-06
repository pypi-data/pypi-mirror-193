# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['monticello', 'monticello.tests', 'monticello.tests.fixtures']

package_data = \
{'': ['*']}

install_requires = \
['morecantile>=3.2.5,<4.0.0',
 'pydelatin>=0.2.7,<0.3.0',
 'pymartini>=0.4.4,<0.5.0',
 'quantized-mesh-encoder>=0.4.3,<0.5.0',
 'titiler.core>=0.11.0,<0.12.0']

setup_kwargs = {
    'name': 'monticello',
    'version': '0.1.0',
    'description': 'Quantized Mesh encoder extension for titiler',
    'long_description': '# Monticello\n\nDynamic quantized mesh encoder extension for [Titiler](https://github.com/developmentseed/titiler).\n\nHeavily adapted from and inspired by [dem-tiler](https://github.com/kylebarron/dem-tiler) \n\nonly partially tested so far...\n\nThe word Monticello means "little mountain" or something close to that in Italian, playing off the naming of titiler to convey smallness \nand topography.\n\n## Features\n\n- supports both delatin and martini algorithms for generating meshes dynamically\n- uses [quantized-mesh-encoder](https://github.com/kylebarron/quantized-mesh-encoder) for response\n- supports variable tile sizes, buffer\n\n\n## Usage\n\n```python\napp = FastAPI()\ntiler = TilerFactory(\n    router_prefix="/cog",\n    extensions = [\n        MonticelloFactory()\n    ]\n)\napp.include_router(tiler.router, prefix="/cog")\n# now meshes are available at /cog/mesh/\n```\n',
    'author': 'Andrew Annex',
    'author_email': 'ama6fy@virginia.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/AndrewAnnex/monticello',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
