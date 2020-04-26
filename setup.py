import sys
from setuptools import setup

setup(
   name='auto-tag-anime',
   version='1.0',
   author='epsp',
   url='https://github.com/Epsp0/auto-tag-anime',
   description='adds tags to anime images predicted by DeepDanbooru tensorflow model',
   install_requires=['tensorflow', 'numpy', 'pillow', 'iptcinfo; platform_system == "Windows"', 
   'xattr; platform_system != "Windows"'],
) 
