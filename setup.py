from setuptools import setup

setup(
    name='agile_food',
    packages=['agile_food'],
    include_package_data=True,
    install_requires=[
        'bs4',
        'requests',
        'flask',
        'pymongo'
    ],
)

