#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
import os
from setuptools import setup, find_packages
<<<<<<< HEAD
#import cloudlb.consts

=======
>>>>>>> 104eb4e582cac11ba83d156a1e025f89cf95682e
NAME = "python-cloudlb"
GITHUB_URL = "https://github.com/rackspace/%s" % (NAME)
DESCRIPTION = "Python interface to Rackspace Load Balancer" + \
    " as a Service product"

def read(fname):
    full_path = os.path.join(os.path.dirname(__file__), fname)
    if os.path.exists(fname):
        return open(full_path).read()
    else:
        return ""

try:
    from cloudlb.consts import VERSION
except ImportError:
    VERSION="0.0.0"
    for line in read('cloudlb/consts.py').split('\n'):
        if line.startswith('VERSION'):
            VERSION = line.split('=')[1].replace('"', '').replace("'", '').strip()

requirements = ['httplib2']

setup(name=NAME,
#      requires=['httplib2',],
#      version=0.1,
#      download_url="%s/zipball/%s" % (GITHUB_URL, '0.1'),
      version=VERSION,
      download_url="%s/zipball/%s" % (GITHUB_URL, VERSION),
      description=DESCRIPTION,
      install_requires=requirements,
      author='Chmouel Boudjnah',
      author_email='chmouel@chmouel.com',
      url=GITHUB_URL,
      long_description=read('README.rst'),
      license='MIT',
      include_package_data=True,
      zip_safe=False,
      scripts=['bin/cloudlb'],
      packages=find_packages(exclude=['tests', 'debian']),
      tests_require=["nose"],
      test_suite="nose.collector",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
        ],
      )
