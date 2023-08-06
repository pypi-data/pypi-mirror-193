"""
Minimal setup.py for compatibility with legacy builds or build tool versions.
"""

from setuptools import setup

setup(name='tahoma',
      version="2.0.7",
      py_modules=['tahoma,get_devices_url'],
      description='API written in Python3 for Somfy Tahoma',
      long_description="This is a very easy API for controlling Somfy Tahoma's devices written in Python3, thanks to the pyoverkiz API. You just need a three-word input to control a device",
      url='https://github.com/pzim-devdata/tahoma',
      license='MIT',
      author='Pzim-devdata',
      author_email='contact@pzim.fr',
      keywords=['tahoma', 'somfy', 'api'],
      packages=['tahoma','tahoma.icons','tahoma.temp'],
      include_package_data = True
      )
