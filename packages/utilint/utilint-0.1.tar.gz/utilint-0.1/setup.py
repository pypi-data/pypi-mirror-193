from setuptools import setup, find_packages

setup(
    name = 'utilint',
    version = '0.1',
    author = 'novitae',
    url = 'https://github.com/novitae/utilint',
    license = 'GNU General Public License v3 (GPLv3)',
    classifiers = [
        'Programming Language :: Python :: 3.10',
    ],
    packages = find_packages(),
    install_requires = ['geopy'],
    description="Turn boring osint data into interesting informations."
)