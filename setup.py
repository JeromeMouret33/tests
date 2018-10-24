from setuptools import setup
import os
import sys



run_cmd = 'pip install git+https://github.com/JeromeMouret33/tests.git@pkg/base_page'

os.system(run_cmd)

setup(
      name='workday',
      version='1.0',
      description='Workday_page specific class for interaction with selenium base_page + locators class',
      author='Jerome Mouret',
      author_email='jerome.mouret@sanofi.com',
      license='SANOFI',
      packages=['workday'],
      zip_safe=False
      )
