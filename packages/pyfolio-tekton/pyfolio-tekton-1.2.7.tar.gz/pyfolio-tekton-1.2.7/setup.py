from setuptools import setup
import pypandoc
import os

folder = 'pyfolio'
helf_path = os.getcwd() + f'/{folder}/README.md'
count_instances = 0
count_instances = helf_path.count('pip-install')

try:
      if count_instances != 1:
            long_description = pypandoc.convert_file(helf_path, 'md')
      else:
            raise "Coudnt Convert README File"
except(FileNotFoundError):
      # long_description = open('README.md').rt,ead()
      raise "Fail README.md dont exists"

setup_kwargs = dict(
      name='pyfolio-tekton',
      version='1.2.7',
      description='PyFolio Tekton',
      packages=[folder],
      author="Quantopian and Everton Mendes",
      author_email="emendes@tektonfinance.com",
      zip_safe=False,
      include_package_data=True
)

if count_instances == 0:
      setup_kwargs['long_description']=long_description,

setup(**setup_kwargs)