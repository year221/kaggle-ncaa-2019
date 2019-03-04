from setuptools import setup
from os import path



setup(
    name='ncaa2019',
    license='MIT',
    version = '0.1.0',    
    description='ncaa 2019 data set and utility functions',
    packages=["ncaa2019"],    
    install_requires=['kaggle', 'pandas>=0.23.0'],
)