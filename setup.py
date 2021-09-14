import pyddragon
import setuptools
from setuptools import setup
import pyddragon


setup(
    name="pyddragon",
    version=pyddragon.__version__,
    author="dp0973",
    author_email="yeong0973@gmail.com",
    description="Python wrapper library providing LoL ddragon data asynchronously",
    license="Apache 2.0",
    packages=setuptools.find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dp0973/pyddragon",
)
