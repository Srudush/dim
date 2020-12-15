from setuptools import setup
from cas import version

setup(name='cas',
      packages=['cas'],
      data_files=[
          ('share/dim-web', glob('www/**', recursive=True)),
          ],
      version=version.VERSION)
