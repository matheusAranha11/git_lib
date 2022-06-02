from setuptools import find_packages, setup


setup(
      name='etl_lib',
      packages=find_packages(include=['etl_lib']),
      version='0.1.14',
      description='Agrupa funções de rotinas de extração, tratamento e armazenamento de dados. ',
      url='git@github.com:matheusAranha11/git_lib.git',
      author='Victor Marchiori, Matheus Lopes',
      license='MIT',
      install_requires=[],
      zip_safe=False
      )

