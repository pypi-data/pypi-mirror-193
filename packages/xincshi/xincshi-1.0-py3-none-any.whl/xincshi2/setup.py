from distutils.core import  setup
import setuptools
packages = ['xincshi2']# 唯一的包名，自己取名
setup(name='xincshi',
	version='1.0',
	author='wjl',
    packages=packages,
    package_dir={'requests': 'requests'},)
