from setuptools import setup, find_packages

setup(
    name="wdsf_api",
    description="WDSF API Python Client",
    version="0.1.0",
    packages=find_packages(),
    license='',
    long_description=open('README.md').read(),
    install_requires=[
        'dacite',
        'requests',
        'xmltodict',
    ],
)