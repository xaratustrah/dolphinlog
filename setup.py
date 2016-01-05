# PyPI setup file

from setuptools import setup, find_packages
from otterlog.version import __version__

classifiers = [
    'Environment :: Console',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Communications :: Ham Radio'
]

setup(
    name='otterlog',
    packages=find_packages(),
    version=__version__,
    description='Yet another HAM radio logger using SQLite with ADIF-3 export support.',
    author='Xaratustra',
    author_email='shahab.sanjari@gmail.com',
    url='https://github.com/xaratustrah/otterlog',  # use the URL to the github repo
    download_url='https://github.com/xaratustrah/otterlog/tarball/{}'.format(__version__),
    entry_points={
        'console_scripts': [
            'otterlog = otterlog.__main__:main'
        ]
    },
    license='GPLv2',
    keywords=['HAM', 'Logging', 'Amateur Radio', 'QSO'],  # arbitrary keywords
    classifiers=classifiers
)
