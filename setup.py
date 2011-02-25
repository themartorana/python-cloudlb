#!/usr/bin/python
# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
import os
from setuptools import setup, find_packages
import cloudlb.consts

NAME = "python-cloudlb"
GITHUB_URL = "https://github.com/chmouel/%s" % (NAME)
DESCRIPTION = "Python interface to Rackspace Load Balancer" + \
    " as a Service product"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name=NAME,
      version=cloudlb.consts.VERSION,
      download_url="%s/zipball/%s" % (GITHUB_URL, cloudlb.consts.VERSION),
      description=DESCRIPTION,
      author='Chmouel Boudjnah',
      author_email='chmouel@chmouel.com',
      url=GITHUB_URL,
      long_description=read('README.rst'),
      license='MIT',
      include_package_data=True,
      zip_safe=False,
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
