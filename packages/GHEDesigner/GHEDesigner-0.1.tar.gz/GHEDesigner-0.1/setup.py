from os import path

from setuptools import setup

from ghedesigner import VERSION

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

short_description = """A dummy ground heat exchanger design tool."""

setup(
    name='GHEDesigner',
    url='https://github.com/mitchute/GHEDesignerPlaceholder',
    description=short_description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=VERSION,
    packages=['ghedesigner'],
    author='Matt Mitchell',
    author_email='mitchute@gmail.com'
)
