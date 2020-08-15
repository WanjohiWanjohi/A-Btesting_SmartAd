from distutils.core import setup

setup(
   name='3Tests',
   version='0.1.0',
   author='An Awesome Coder',
   author_email='aac@example.com',
   packages=['package_name', 'package_name.test'],
   scripts=['bin/script1','bin/script2'],
   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   long_description=open('README.txt').read(),
   install_requires=[
       "pandas",
       "csv",
      "seaborn",
     "scipy",
     "imblearn"
   ],
)
