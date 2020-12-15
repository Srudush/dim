from setuptools import setup

setup(name='cas',
      packages=['cas'],
      data_files=[
          {'share/dim-web', ['dist/index.html']},
          {'share/dim-web/css', ['dist/css']},
          {'share/dim-web/js', ['dist/js']},
          {'share/dim-web/images', ['dist/images']},
          {'share/dim-web/font-awesome-4.7.0', ['dist/font-awesome-4.7.0']},
          ],
      version='0.1')
