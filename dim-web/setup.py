from setuptools import setup
import glob
from cas import version

setup(name='cas',
      packages=['cas'],
      data_files=[
          ('share/dim-web', glob.glob('www/**.*', recursive=True)),
          ],
      version=version.VERSION)
