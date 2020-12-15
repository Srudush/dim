from setuptools import setup
from cas import version

setup(name='cas',
      packages=['cas'],
      data_files=[
          ('share/dim-web', ['www/index.html']),
          ('share/dim-web/static', ['www/css']),
          ],
      version=version.VERSION)
