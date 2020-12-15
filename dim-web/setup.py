from setuptools import setup
from cas import version

setup(name='cas',
      packages=['cas'],
      data_files=[
          ('share/dim-web', ['www/index.html']),
          ('share/dim-web/css', ['www/css']),
          ('share/dim-web/js', ['www/js']),
          ('share/dim-web/images', ['www/images']),
          ('share/dim-web/font-awesome-4.7.0', ['www/font-awesome-4.7.0']),
          ],
      version=version.VERSION)
