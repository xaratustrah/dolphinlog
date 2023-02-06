# dolphinlog
<img src="https://github.com/xaratustrah/dolphinlog/raw/main/rsrc/dolphin.png" width=“128”>

This program has been renamed to `dolphinlog` to avoid naming conflict with another package.

This is a log program for amateur radio [(HAM)](https://en.wikipedia.org/wiki/Amateur_radio) operators for daily use. There are tons of HAM log programs out there. This is yet another one, aiming to be free, modern but as well ultra simple by using only the command line interface in order to store QSO data in a SQLite database. An export function to ADIF-3 \*.adi is also available.

There are no editors, this means that the database file should be viewed using standard viewer programs, of which also many exist. Some examples are standalone programs such as [sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser) or browser plugins such as [this one](https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/). This leaves the HAM a great deal of freedom to import, export in/to any format and manage the database. The typical usage of such a log program is for running on an ideally small or embedded computer such as [RaspberryPi2](https://en.wikipedia.org/wiki/Raspberry_Pi), as a HAM computer, where possibly also other HAM related software such as [fldigi](https://sourceforge.net/projects/fldigi/) are running, or HAM related hardware attached, such as [dongles](http://www.funcubedongle.com/) are also running. The name of this program is inspired by other HAM radio logger software available on the internet that have an animal name
in their title.

#### Installation

`dolphinlog` is by nature platform independent. The simplest way to install it is to use PyPI:

    pip install dolphinlog

Other than that `dolphinlog` needs just a working Python 3 installation. So whatever OS you have, just put the script
somewhere you can call it, e.g. by symbolic linking like this:
 
    ln -s dolphinlog /usr/local/bin/dolphinlog

#### Usage
Just type:

    dolphinlog
    
In the command line and the program starts. If you like to skip an entry, just press enter. If no command line arguments are given at invocation time, then the program creates a folder in the home directory:

    ~/.dolphinlog/dolphinlog.sqlite

otherwise a specific database filename can be given by the `-db` switch. `-v` switch increases the verbosity. If the switch `-adi` is provided, then an `*.adi` file is exported. For this export either the default database file name is used, or a database filename should be given.

#### DB Fields and ADIF-3 export


`dolphinlog` supports export to function to the ADIF3 \*.adi format. The [ADIF 3](http://adif.org/) standard has a very comprehensive list of fields. In order to find a minimalistic implementation of export function, `dolphinlog` adapts the minimum ADIF record fields required by the website [eQSL](https://www.eqsl.cc), but also includes additional fields. Minimum ADIF-3 fields required by eQSL:

|Field  |  Description|
|-------|-------------|
|QSO_DATE| date on which the QSO started YYYYMMDD|
|TIME_ON| QSO time in UTC|
|CALL| the contacted station's Callsign|
|MODE| QSO Mode|
|BAND| QSO Band|

ADIF-3 fields fields recommended by eQSL:

|Field  |  Description|
|-------|-------------|
|FREQ| QSO frequency in Megahertz|
|PROP_MODE| QSO propagation mode|
|PROGRAMID| identifies the name of the logger, converter, or utility that created or processed this ADIF file|
|QSLMEG| QSL card message|
|RST_SENT| signal report sent to the contacted station|


ADIF-3 fields additionally used by `dolphinlog`:

|Field  |  Description|
|-------|-------------|
| NAME | the contacted station's operator's name |
| RST_RCVD | signal report from the contacted station|
|RX_PWR | the contacted station's transmitter power in watts|
|TX_PWR | the logging station's power in watts|
|GRIDSQUARE | the contacted station's 2-character, 4-character, 6-character, or 8-character Maidenhead Grid Square|
|NOTES | QSO Notes|


That’s basically it folks. Enjoy.
