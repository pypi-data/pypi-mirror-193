from setuptools import setup, find_packages

from datahub_py import __version__

setup(
    name='datahub_py',
    version=__version__,
    description='Datahub core',

    url='https://github.com/26medias/Datahub-py',
    author='Julien L',
    author_email='julien@leap-forward.ca',

    packages=find_packages(exclude=['tests', 'tests.*']),

    extras_require={
        'flask': ['Flask==2.2.2', 'Flask_RESTful==0.3.9'],
        'numpy': ['numpy==1.23.5'],
        'requests': ['requests==2.28.1']
    },

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
