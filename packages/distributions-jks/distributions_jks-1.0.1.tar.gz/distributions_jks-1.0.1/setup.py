from setuptools import setup
from pathlib import Path

this_diectory = Path(__file__).parent
long_description = (this_diectory / "README.md").read_text()

setup(name='distributions_jks',
      version='1.0.1',
      long_description=long_description,
      long_description_content_type = 'text/markdown',
      packages=['distributions_jks'],
      author='Jaya Krishna with Udacity',
      author_email='jayakrishnas.work@gmail.com',
      requires=['matplotlib', 'math'],
      zip_safe=False)
