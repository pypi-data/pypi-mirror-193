from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='xpflow',
      version='v0.0.1',
      description='Pandas with some cool additional features',
      url='https://github.com/sileod/pandit',
      author='sileod',
      license='GPL',
      install_requires=['pandas'],
      py_modules=['pandit'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)
