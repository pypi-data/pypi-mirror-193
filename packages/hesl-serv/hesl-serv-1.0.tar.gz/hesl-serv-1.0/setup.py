from setuptools import setup, find_packages
from os.path import join, dirname
import heslserv

setup(
    name='hesl-serv',
    version=heslserv.__version__,
    author='LowLevelCoder',
    author_email='flat.assembly@gmail.com',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['server = heslserv.server:run_server']
    },
    install_requires=[
	'Flask'
    ]
)
