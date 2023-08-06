from setuptools import setup, find_packages


setup(
    name='beautifultxt',
    version='1',
    license='MIT',
    author="Beautiful Text Official",
    author_email='kxekip@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='colors',
    install_requires=[
          'colorama',
          'zipfile',
          'requests',
      ],

)