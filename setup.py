from setuptools import setup

setup(name='workday',
      version='1.0',
      description='Workday_page specific class for interaction with selenium base_page + locators class',
      author='Jerome Mouret',
      author_email='jerome.mouret@sanofi.com',
      license='SANOFI',
      packages=['workday'],
      dependency_links=['https://github.com/JeromeMouret33/tests.git@pkg/base_page'],
      zip_safe=False)
