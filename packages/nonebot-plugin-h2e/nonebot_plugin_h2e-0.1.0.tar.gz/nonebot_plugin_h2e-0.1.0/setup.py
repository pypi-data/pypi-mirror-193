import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '0.1.0'
DESCRIPTION = 'a nonebot2 plugin package for how to exercise '
LONG_DESCRIPTION = ' how 2 exercise 如何锻炼——Bot已经帮我们解决了吃什么 能不能解决我们练什么呢。其中包含 健身、游泳、瑜伽 三类运动，并提供了一些运动方法。  '

# Setting up
setup(
    name="nonebot_plugin_h2e",
    version=VERSION,
    author="Gin2O",
    author_email="wulun0102@outlook.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[]
)
