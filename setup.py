from setuptools import setup, find_packages

setup(
    name='tableau_tools',
    version='3.0.1',
    install_requires=['lxml'],
    packages=find_packages(),
    url='https://github.com/bryantbhowell/tableau_tools',
    license='',
    author='Bryant Howell',
    author_email='bhowell@tableau.com',
    description='A library for programmatically working with Tableau files and Tableau Server, including the REST API'
)
