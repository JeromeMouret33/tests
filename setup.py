from setuptools.command.install import install as _install
from setuptools import setup, find_packages
import pip

class install(_install):
  def run(self):
    _install.do_egg_install(self)

    # just go ahead and do it
    pip.main(['install', 'https://github.com/JeromeMouret33/tests.git@pkg/base_page'])



setup(
      name='workday',
      version='1.0',
      description='Workday_page specific class for interaction with selenium base_page + locators class',
      author='Jerome Mouret',
      author_email='jerome.mouret@sanofi.com',
      license='SANOFI',
      packages=['workday'],
      cmdclass={'install': install},
      zip_safe=False
      )
