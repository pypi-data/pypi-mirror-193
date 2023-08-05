from distutils.core import  setup
import setuptools
packages = ['graph2topictm']# 唯一的包名，自己取名
setup(name='graph2topictm',
	version='1.2',
    description='Graph2Topic is a topic model based on PLMs and community detections. more details in https://github.com/lunar-moon/Graph2Topic.git',
	author='ljp',
    author_email='313446266@qq.com',
    packages=setuptools.find_packages()
    )
