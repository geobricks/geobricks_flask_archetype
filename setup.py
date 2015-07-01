from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksFlaskArchetype',
    version='0.1.7',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Archetype based on Flask and Blueprints to be used for Geobricks services.',
    install_requires=[
        'watchdog', 'flask', 'flask-cors'
    ],
    url='http://pypi.python.org/pypi/GeobricksFlaskArchetype/'
)
