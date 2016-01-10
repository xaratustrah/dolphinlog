# PyPI setup file

from setuptools import setup, find_packages
from dolphinlog.version import __version__

# try:
#     import pypandoc
#
#     long_description = pypandoc.convert('README.md', 'rst')
# except(IOError, ImportError):
#     long_description = open('README.md').read()

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
    name='dolphinlog',
    packages=find_packages(),
    version=__version__,
    description='Yet another HAM radio logger using SQLite with ADIF-3 export support.',
    #long_description=long_description,
    author='Xaratustra',
    author_email='shahab.sanjari@gmail.com',
    url='https://github.com/xaratustrah/dolphinlog',  # use the URL to the github repo
    download_url='https://github.com/xaratustrah/dolphinlog/tarball/{}'.format(__version__),
    entry_points={
        'console_scripts': [
            'dolphinlog = dolphinlog.__main__:main'
        ]
    },
    license='GPLv2',
    keywords=['HAM', 'Logging', 'Amateur Radio', 'QSO'],  # arbitrary keywords
    classifiers=classifiers
)
