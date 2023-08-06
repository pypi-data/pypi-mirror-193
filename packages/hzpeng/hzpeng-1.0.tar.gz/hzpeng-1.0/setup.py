from distutils.core import  setup
import setuptools
packages = ['hzpeng']# 唯一的包名，自己取名
setup(name='hzpeng',
	version='1.0',
	author='hzpeng',
    packages=packages, 
    package_dir={'requests': 'requests'},)

