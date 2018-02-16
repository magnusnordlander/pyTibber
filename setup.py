from setuptools import setup

long_description = None
with open("README.md", 'r') as fp:
    long_description = fp.read()

setup(
    name = 'pyTibber',
    packages = ['tibber'],
    install_requires=['gql==0.1.0', 'aiohttp==2.2.5', 'async_timeout==1.4.0'],
    version='0.3.0',
    description='A python3 library to communicate with Tibber',
    long_description=long_description,
    author='Daniel Hoyer Iversen',
    author_email='mail@dahoiv.net',
    url='https://github.com/Danielhiversen/pyTibber',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
