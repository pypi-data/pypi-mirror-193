#!/usr/bin/python3
from setuptools import setup
import os
with open('PYPI_README.md') as f:
    long_description = f.read()
exec((open(os.path.dirname(os.path.abspath(__file__))+"/tahoma/__version__.py")).read())

setup(name='tahoma',
      version=__version__,
      python_requires=">=3.7",
      py_modules=['tahoma,ext_modules,test'],
      description='API written in Python3 for Somfy Tahoma',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/pzim-devdata/tahoma',
      license='MIT',
      author='Pzim-devdata',
      author_email='contact@pzim.fr',
      keywords=['tahoma', 'somfy', 'api'],
      packages=['tahoma','tahoma.icons','tahoma.temp','tahoma.ext_modules','tahoma.test'],
      include_package_data = True,
      entry_points={
        'console_scripts': [
            'tahoma=tahoma:main',
            'get_devices_url=get_devices_url:main',
            'install_tahoma=install_tahoma.py:main'
        ]
      },
      install_requires = [
      'pyoverkiz==1.7.4',
      'asyncio',
      'sys',
      'argparse',
      'os',
      're',
      'getpass',
      'time'
      ]

      )
