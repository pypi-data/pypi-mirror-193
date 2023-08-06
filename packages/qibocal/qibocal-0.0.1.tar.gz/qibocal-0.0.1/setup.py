# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qibocal',
 'qibocal.calibrations',
 'qibocal.calibrations.characterization',
 'qibocal.calibrations.niGSC',
 'qibocal.calibrations.niGSC.basics',
 'qibocal.cli',
 'qibocal.fitting',
 'qibocal.plots',
 'qibocal.tests',
 'qibocal.web']

package_data = \
{'': ['*'], 'qibocal.web': ['static/*', 'templates/*']}

install_requires = \
['Pint-Pandas>=0.3,<0.4',
 'dash>=2.6.0,<3.0.0',
 'lmfit>=1.0.3,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'qibo>=0.1.9,<0.2.0',
 'qibolab>=0.0.1,<0.0.2']

extras_require = \
{'docs': ['Sphinx>=4.3.2,<5.0.0',
          'furo>=2022.9.29,<2023.0.0',
          'sphinxcontrib-bibtex>=2.4.1,<3.0.0',
          'recommonmark>=0.7.1,<0.8.0',
          'sphinx_markdown_tables>=0.0.17,<0.0.18']}

entry_points = \
{'console_scripts': ['qq = qibocal:command',
                     'qq-compare = qibocal:compare',
                     'qq-live = qibocal:live_plot',
                     'qq-upload = qibocal:upload']}

setup_kwargs = {
    'name': 'qibocal',
    'version': '0.0.1',
    'description': '',
    'long_description': '# Qibocal\n![Tests](https://github.com/qiboteam/qibocal/workflows/Tests/badge.svg)\n[![codecov](https://codecov.io/gh/qiboteam/qibocal/branch/main/graph/badge.svg?token=1EKZKVEVX0)](https://codecov.io/gh/qiboteam/qibo)\n[![Documentation Status](https://readthedocs.org/projects/qibocal/badge/?version=latest)](https://qibocal.readthedocs.io/en/latest/)\n\nQibocal provides Quantum Characterization Validation and Verification protocols using [Qibo](https://github.com/qiboteam/qibo) and [Qibolab](https://github.com/qiboteam/qibolab).\n\nQibocal key features:\n\n- Automatization of calibration routines.\n\n- Declarative inputs using runcard.\n\n- Generation of a report.\n\n## Installation\n\nThe package can be installed by source:\n```sh\ngit clone https://github.com/qiboteam/qibocal.git\ncd qibocal\npip install .\n```\n\n\n### Developer instructions\nFor development make sure to install the package using [`poetry`](https://python-poetry.org/) and to install the pre-commit hooks:\n```sh\ngit clone https://github.com/qiboteam/qibocal.git\ncd qibocal\npoetry install\npre-commit install\n```\n\n## Minimal working example\n\nThis section shows the steps to perform a resonator spectroscopy with Qibocal.\n### Write a runcard\nA runcard contains all the essential information to run a specific task.\nFor our purposes, we can use the following:\n```yml\nplatform: tii1q\n\nqubits: [0]\n\nformat: csv\n\nactions:\n   resonator_spectroscopy:\n     lowres_width: 5_000_000\n     lowres_step: 2_000_000\n     highres_width: 1_500_000\n     highres_step: 200_000\n     precision_width: 1_500_000\n     precision_step: 100_000\n     software_averages: 1\n     points: 5\n```\n### Run the routine\nTo run all the calibration routines specified in the ```runcard```, Qibocal uses the `qq` command\n```sh\nqq <runcard> -o <output_folder>\n```\nif ```<output_folder>``` is specified, the results will be saved in it, otherwise ```qq``` will automatically create a default folder containing the current date and the username.\n\n### Visualize the data\n\nQibocal gives the possibility to live-plotting with the `qq-live` command\n```sh\nqq-live <output_folder>\n```\n### Uploading reports to server\n\nIn order to upload the report to a centralized server, send to the server administrators your public ssh key (from the machine(s) you are planning to upload the report) and then use the `qq-upload <output_folder>` command. This program will upload your report to the server and generate an unique URL.\n\n## Contributing\n\nContributions, issues and feature requests are welcome!\nFeel free to check\n<a href="https://github.com/qiboteam/qibocal/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues-closed/qiboteam/qibocal"/></a>\n',
    'author': 'andrea-pasquale',
    'author_email': 'andreapasquale97@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/qiboteam/qibocal/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
