from setuptools import setup, find_packages

setup(
    name='basicfoncier',
    packages=find_packages(exclude=['test', 'tests']),
    description='Basic Foncier',
    long_description='Basic Foncier : traitement de données cadastrales et foncières',
    version='0.1',
    python_requires='>=3.7',
    install_requires=[
        'setuptools~=60.2.0',
        'pandas~=2.1.3',
        'numpy~=1.26.1'
    ],
    url='http://github.com/PiouPiou974/basicfoncier',
    author='Antoine PETIT',
    author_email='antoine.petit@lilo.org',
    keywords=['pip', 'basicfoncier', 'foncier']
)
