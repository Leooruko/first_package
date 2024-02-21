from setuptools import setup,find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Leooruko/mypackage',
    author='Leon Oruko', 
    author_email='orukoleon94@gmail.com'
)

# python setup.py sdist bdist_wheel --universal 

