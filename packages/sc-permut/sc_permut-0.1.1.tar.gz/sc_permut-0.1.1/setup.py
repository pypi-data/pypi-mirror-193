# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sc_permut']

package_data = \
{'': ['*']}

install_requires = \
['keras==2.4.3',
 'kopt==0.1.0',
 'py4j>=0.10.9.7,<0.11.0.0',
 'pyyaml==5.3.1',
 'scanpy==1.6.0',
 'tensorflow==2.3.1']

entry_points = \
{'console_scripts': ['sc_permut = sc_permut.__main__:main']}

setup_kwargs = {
    'name': 'sc-permut',
    'version': '0.1.1',
    'description': 'Deep learning annotation of cell-types with permutation inforced autoencoder',
    'long_description': '# sc_permut\nDeep learning annotation of cell-types with permutation inforced autoencoder\n\n\n\n## Summary\n\n### Parse Scanpy, Seurat and CellRanger objects\n\nFast crawl through your folder and detect Seurat (.rds), Scanpy (.h5ad) or cellranger (.h5) atlas files.\n\n## Usage\n\nThe one liner way to run checkatlas is the following: \n\n```bash\n$ cd your_search_folder/\n$ python -m sc_permut .\n#or\n$ checkatlas .\n```\n\nOr run it inside your python workflow.\n\n```py\nfrom sc_permut import sc_permut\nsc_permut.run(path, atlas_list, multithread, n_cpus)\n```\n\n\n## Development\n\nRead the [CONTRIBUTING.md](docs/contributing.md) file.',
    'author': 'becavin-lab',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://sc_permut.readthedocs.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
