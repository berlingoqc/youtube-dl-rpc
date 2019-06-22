from setuptools import setup, find_packages


setup(
    name='youtube-dl-rpc',
    version='0.0.1',
    description='Daemon implementation of youtubdl with rpc and ws',
    packages=find_packages(exclude=('test'))
)
