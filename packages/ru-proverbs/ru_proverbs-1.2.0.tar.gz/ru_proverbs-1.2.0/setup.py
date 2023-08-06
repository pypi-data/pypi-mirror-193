# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ru_proverbs']

package_data = \
{'': ['*']}

install_requires = \
['tensorflow>=2.3.1,<3.0.0', 'textgenrnn>=2.0.0,<3.0.0']

entry_points = \
{'console_scripts': ['ru-proverbs = ru_proverbs.__main__:main',
                     'ru_proverbs = ru_proverbs.__main__:main']}

setup_kwargs = {
    'name': 'ru-proverbs',
    'version': '1.2.0',
    'description': 'Russian Proverbs AI-powered proverbs generator.',
    'long_description': 'RU Proverbs AI module\n-------\n[![PyPI version](https://badge.fury.io/py/ru-proverbs.svg)](https://badge.fury.io/py/ru-proverbs)\n\nThis module provides API that allows generating Russian Proverbs with the power of AI.\n\n# Requirements\n\nFor Windows builds:\n\nIn the current version we use Python 3.10.4, Tensorflow 2.3.1 and CUDA 10.1.\n\n1. Python 3.10.x x64 (tested with [Python 3.10.4x64][python]).\n\n2. [Poetry][poetry].\n\n3. Install dependencies:\n\n   2.1 Install dependencies and virtual env: `poetry install`.\n\n   2.2 Optionally install and configure CUDA support.\n\n## Configure CUDA\n\n1. Download [CUDA Toolkit][cuda-toolkit] and unpack into e.g. `D:\\DevTools\\cuda\\v10.1`.\n\n2. Download matching [cuDNN][cuDNN] version (e.g. v7.6.5 for CUDA 10.1) and unpack under the\n   versioned CUDA folder, e.g. `D:\\DevTools\\cuda\\v10.1\\cudnn`.\n\n3. Add CUDA paths to environment variables and `PATH`:\n\n   Create `CUDA_HOME` and `CUDA_PATHS` env variables with the following values:\n    ```cmd\n    SET CUDA_HOME=D:\\DevTools\\cuda\\v10.1\n    SET CUDA_PATHS=%CUDA_HOME%\\bin;%CUDA_HOME%\\include;%CUDA_HOME%\\extras;%CUDA_HOME%\\libnvvp;%CUDA_HOME%\\cudnn\\bin;\n    ```\n\n   Add `CUDA_PATHS` to `PATH`: `SET PATH=%CUDA_PATHS%;%PATH%`.\n\n[python]: https://www.python.org/downloads/release/python-3104/\n\n[poetry]: https://python-poetry.org/\n\n[tensorflow]: https://www.tensorflow.org/install/pip\n\n[cuda-toolkit]: https://developer.nvidia.com/cuda-10.1-download-archive-update2?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal\n\n[cuDNN]: https://developer.nvidia.com/rdp/cudnn-download\n',
    'author': 'Yurii Serhiichuk',
    'author_email': 'savik.ne@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xSAVIKx/ru-proverbs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10.0,<3.11.0',
}


setup(**setup_kwargs)
