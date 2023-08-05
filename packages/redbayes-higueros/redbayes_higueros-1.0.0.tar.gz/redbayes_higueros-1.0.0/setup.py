import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.0' 
PACKAGE_NAME = 'redbayes_higueros'  
AUTHOR = 'Angel Higueros'
AUTHOR_EMAIL = 'hig20460@uvg.edu.gt'
URL = 'https://github.com/angelhigueros11/ia-lab2'

LICENSE = 'MIT'
DESCRIPTION = 'Implementación de Red de Bayes sin utilizar librerias externas'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      'numpy',
      'matplotlib',
      'networkx'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)