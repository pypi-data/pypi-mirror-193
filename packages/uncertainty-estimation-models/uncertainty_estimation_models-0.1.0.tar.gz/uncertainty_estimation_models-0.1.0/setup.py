# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uncertainty_estimation']

package_data = \
{'': ['*']}

install_requires = \
['MAPIE==0.5.0',
 'gluonts==0.11.8',
 'lightgbm==3.3.2',
 'numba==0.56.4',
 'pandas==1.3.5',
 'pgbm==1.8.0',
 'properscoring==0.1',
 'pytorch_lightning==1.8.4',
 'scikit-learn==1.0.2',
 'torch==1.13.1',
 'xgboost==1.6.2']

extras_require = \
{':python_full_version >= "3.7.1" and python_version < "3.11"': ['ngboost==0.3.13'],
 ':python_version >= "3.8" and python_version < "3.11"': ['numpy==1.21.2',
                                                          'pytorch-forecasting==0.10.3',
                                                          'scipy==1.8.0']}

setup_kwargs = {
    'name': 'uncertainty-estimation-models',
    'version': '0.1.0',
    'description': 'This is the main library for the uncertainty estimation project.',
    'long_description': '# Introduction \nTODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. \n\n# Getting Started\nTODO: Guide users through getting your code up and running on their own system. In this section you can talk about:\n1.\tInstallation process\n2.\tSoftware dependencies\n3.\tLatest releases\n4.\tAPI references\n\n# Build and Test\nTODO: Describe and show how to build your code and run the tests. \n\n# Contribute\nTODO: Explain how other users and developers can contribute to make your code better. \n\nIf you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:\n- [ASP.NET Core](https://github.com/aspnet/Home)\n- [Visual Studio Code](https://github.com/Microsoft/vscode)\n- [Chakra Core](https://github.com/Microsoft/ChakraCore)',
    'author': 'Jonas Flor, Florian Günther, Sándor Daróczi, Slava Kisilevich',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
