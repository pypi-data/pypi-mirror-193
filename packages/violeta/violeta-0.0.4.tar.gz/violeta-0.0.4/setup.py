# encoding: utf-8
# Modificado para o padrão novo em 07/06/2019 - Denis Urbanavicius

from setuptools import setup, find_packages
import io
import os
import re


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(name='violeta',
      version = "0.0.4",
      setup_requires=["setuptools-git-version"],
      description="Reusable functions for Captalys projects.",
      long_description=read("README.rst"),
      url="https://github.com/Captalys/violeta.git",
      author="Bruno FS",
      author_email="bruno.souza@captalys.com.br",
      license="BSD",
      keywords="captalys platform",
      packages=find_packages(),
      package_data={
          'violeta': ['data/ANBIMA.txt'],
          'violeta.config': ['*.ini'],
          'violeta.tests': ['*/*.json', '*/*.xml']
      },
      install_requires=[
        'bizdays==1.0.8',
        'bs4==0.0.1',
        'jsonschema>=3.0.1,<=3.2.0',
        'numpy==1.19.5',
        'pandas==1.1.5',
        'requests==2.26.0',
        'scipy==1.5.4',
        'simplejson==3.17.2',
        'suds-py3==1.4.4.1',
        'xmltodict==0.12.0'
      ],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      zip_safe=False
      )
