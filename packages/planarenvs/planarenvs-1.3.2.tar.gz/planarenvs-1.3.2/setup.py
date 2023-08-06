# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['planarenvs',
 'planarenvs.mobile_base',
 'planarenvs.mobile_base.envs',
 'planarenvs.mobile_robot',
 'planarenvs.mobile_robot.envs',
 'planarenvs.n_link_reacher',
 'planarenvs.n_link_reacher.envs',
 'planarenvs.n_link_reacher.resources',
 'planarenvs.planar_common',
 'planarenvs.point_robot',
 'planarenvs.point_robot.envs',
 'planarenvs.scenes',
 'planarenvs.sensors']

package_data = \
{'': ['*']}

install_requires = \
['forwardkinematics>=1.0.3,<2.0.0',
 'gym>=0.22,<0.23',
 'mpscenes>=0.3,<0.4',
 'numpy>=1.19,<1.24',
 'pygame>=2.1.2,<3.0.0',
 'pyglet>=1.5.21,<2.0.0',
 'pylint>=2.13.3,<3.0.0',
 'scipy>=1.5,<2.0']

setup_kwargs = {
    'name': 'planarenvs',
    'version': '1.3.2',
    'description': 'Lightweight open-ai gym environments for planar kinematic chains.',
    'long_description': 'None',
    'author': 'Max Spahn',
    'author_email': 'm.spahn@tudelft.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
