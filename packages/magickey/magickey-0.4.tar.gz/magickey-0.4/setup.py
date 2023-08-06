from setuptools import setup

setup(name='magickey',
      version='0.4',
      description='This module provides iPython integration and magics that allow exact, inexact and intellegent code execution.',
      url='https://gitlab.com/mcaledonensis/magickey',
      author='Merlinus Caledonensis',
      author_email='merlin@roundtable.game',
      license='Apache 2.0',
      packages=['magickey'],
      package_data={'': ['prompt.txt']},
      include_package_data=True,
      zip_safe=False)
