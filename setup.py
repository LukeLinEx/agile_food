from setuptools import setup

setup(
    name='online',
    packages=['online'],
    include_package_data=True,
    install_requires=[
        'bs4',
        'requests',
        'flask',
        'pymongo'
    ],
)