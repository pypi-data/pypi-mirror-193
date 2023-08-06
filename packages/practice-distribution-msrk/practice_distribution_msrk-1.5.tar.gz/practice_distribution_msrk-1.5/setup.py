from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory/"readme.md").read_text()

setup(name='practice_distribution_msrk',
      version='1.5',
      description='Gaussian distributions',
      packages=['practice_distribution_msrk'],
      zip_safe=False,
      author='Satya Rohith Kumar',
      author_email='rohithmeduri24@gmail.com',
      requires=['matplotlib','math'],
      long_description = long_description,
      long_description_content_type = 'text/plain')
