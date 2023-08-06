import setuptools

with open('README.rst', 'r') as file:
    README = file.read()

with open('requirements.txt', 'r') as file:
    requirements = file.read().splitlines(keepends=False)

setuptools.setup(
    name='archivist-logger',
    version='0.1.0',
    description="Fast building of logger from common templates.",
    long_description=README,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    include_package_data=True,
    author='Romain Damian',
    author_email='damian.romain@gmail.com',
    url='https://gitlab.com/roam-packages/archivist.git'
)
