# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neurobooth']

package_data = \
{'': ['*']}

install_requires = \
['h5io>=0.1.7,<0.2.0',
 'jupyter>=1.0.0,<2.0.0',
 'jupyterlab>=2.2.9,<3.0.0',
 'matplotlib>=3.3.3,<4.0.0',
 'mediapipe==0.8.9.1',
 'moviepy>=1.0.3,<2.0.0',
 'opencv-python>=4.7.0,<5.0.0',
 'transformers>=4.0.0,<5.0.0',
 'wget>=3.2,<4.0']

setup_kwargs = {
    'name': 'neurobooth',
    'version': '0.1.0',
    'description': 'A python library and framework for fast neural network computations.',
    'long_description': '# Landmark Detection\n\nNeurobooth library for landmark detection of face features, face mesh, pose, etc. \n\nInstallable with `pip install neurobooth`\n\nIf you have docker and docker-compose installed, you can run the following to set up a jupyter environment:\n\n```\ndocker-compose build\ndocker-compose up\n```',
    'author': 'Andrew Chang',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/neurobooth/landmark-detection',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
