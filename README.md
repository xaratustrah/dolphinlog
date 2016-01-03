# otterlog
<img src="https://github.com/xaratustrah/otterlog/blob/master/rsrc/otter.png" width=“128”>

This is a log program for amateur radio [(HAM)](https://en.wikipedia.org/wiki/Amateur_radio) operators for daily use.
There are tons of HAM log programs out there. This is yet another one, aiming to be ultra simple by using
only the command line interface in order to store QSO data in a SQLite database. There are no editors,
this means that the database file should be viewed using standard viewer programs, of which also many exist.
Some examples are standalone programs such as [sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser) or browser
plugins such as [this one](https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/). This
leaves the HAM a great deal of freedom to import, export in/to any format and manage the database.

The typical usage of such a log program is for running on an ideally small or embedded computer such as
[RaspberryPi2](https://en.wikipedia.org/wiki/Raspberry_Pi), as a HAM computer, where possibly also other HAM related
software such as [fldigi](https://sourceforge.net/projects/fldigi/) are running, or HAM related hardware attached, such
as [dongles](http://www.funcubedongle.com/) are also running.

The name of this program is inspired by other HAM radio logger software available on the internet that have an animal name
in their title.

#### Installation

`otterlog` is by nature platform independent. The simplest way to install it is to use PyPI:

    pip install otterlog

Other than that `otterlog` needs just a working Python 3 installation. So whatever OS you have, just put the script
somewhere you can call it, e.g. by symbolic linking like this:
 
    ln -s otterlog /usr/local/bin/otterlog

#### Usage
Just type:

    otterlog
    
In the command line and the program starts. If you like to skip an entry, just press enter. If no command line arguments
are given at invocation time, then the program creates a folder in the home directory:

    ~/.otterlog/otterlog.sqlite

otherwise a specific database filename can be given by the `-f` switch. `-v` switch increases the verbosity.
