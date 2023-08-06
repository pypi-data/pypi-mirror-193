from setuptools import setup, find_packages

setup(
    name='oldmango',
    version='0.1',
    description='Linux commands AI',
    packages=find_packages(),
    install_requires=[
        'openai>=1.0',
        'click>=2.0',
        'requests>=2.0'
    ]
)

