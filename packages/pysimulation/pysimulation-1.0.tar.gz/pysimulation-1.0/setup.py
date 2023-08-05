from setuptools import setup

setup(
    name = 'pysimulation',
    version = '1.0',
    author = 'rakson',
    license = 'MIT',
    py_modules = ['simulation'],
    install_requires = [
        'pandas',
        'pytz'
    ],
)