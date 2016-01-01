# PyPI setup file

from otterlog.version import __version__
from distutils.core import setup

classifiers = [
    'Environment :: Console',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Intended Audience :: Information Technology',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Communications :: Ham Radio'
]

setup(
    name='otterlog',
    packages=['otterlog'],  # this must be the same as the name above
    version=__version__,
    description=' Yet another HAM logger using SQLite',
    author='Xaratustra',
    author_email='shahab.sanjari@gmail.com',
    url='https://github.com/xaratustrah/otterlog',  # use the URL to the github repo
    download_url='https://github.com/xaratustrah/otterlog/tarball/{}'.format(__version__),
    scripts=['otterlog'],
    license='GPL v2',
    keywords=['HAM', 'Logging', 'Amateur Radio', 'QSO'],  # arbitrary keywords
    classifiers=classifiers,
)
