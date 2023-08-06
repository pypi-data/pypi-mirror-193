from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='shacrypt',
  version='0.0.1',
  description='SHA256 Encryption Algorithm.',
  long_description='SHA256 is Encryption Algorithm for encrypting certain values. It was created by The National Security Agency and this is my implementation for the Python programming language.',
  url='',  
  author='64biit',
  author_email='sixtyfourblit@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=find_packages(),
  install_requires=[''] 
)
