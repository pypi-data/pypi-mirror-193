from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='gtja-vintex-qyt',
    version='1.0.6',
    keywords='gtja-vintex-qyt',
    description='Python Library for GTJA Vintex QYT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alfred42/gtja-qyt-python-lib',
    author='Liang Shi',
    author_email='shiliang022975@gtjas.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['vintex.pub', 'libGtjaCommon.dll', 'libGtjaCommon.so'],
    },
    platforms='any',
    install_requires=[
        'certifi>=2022.9.14',
        'charset-normalizer>=2.1.1',
        'idna>=3.4',
        'requests>=2.28.1',
        'urllib3>=1.26.12',
        'pandas>=1.3.5',
        'pycryptodome>=3.16.0'
    ],
)
