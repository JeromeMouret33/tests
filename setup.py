from setuptools import setup

setup(name='base_page',
      version='1.0',
      description='Base page + Web driver object with the selenium functions',
      author='Jerome Mouret',
      author_email='jerome.mouret@sanofi.com',
      license='SANOFI',
      packages=['base_page'],
      install_requires=[
          'selenium',
          'time'
      ],
      zip_safe=False)
