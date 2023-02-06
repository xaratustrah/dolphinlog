#!/usr/bin/env python
"""
Yet another HAM radio logger using SQLite.

Dec 2015 - xaratustra

"""

import argparse
import logging as log
import os
import sys
import datetime
from dolphinlog.version import __version__
from dolphinlog.qsodata import QSOData


def fill_in_data(qso_data):
    print('Enter to leave field empty. ctrl-c or ctrl-d to abort.\n')
    try:
        qso_data.qso_date = input('UTC Date YYYYMMDD [empty for today]: ')
        if qso_data.qso_date == '':
            qso_data.qso_date = datetime.datetime.utcnow().strftime('%Y%m%d')
        qso_data.time_on = input('UTC time HHMM [empty for just now]: ')
        if qso_data.time_on == '':
            qso_data.time_on = datetime.datetime.utcnow().strftime('%H%M')
        qso_data.call = input('OM\'s call sign: ')
        qso_data.name = input('OM\'s name : ')
        qso_data.gridsquare = input('OM\'s locator : ')
        qso_data.mode = input('Mode : ')
        qso_data.band = input('Band : ')

        while True:
            qso_data.freq = input('Frequncy : ')
            if not qso_data.freq == '':
                try:
                    qso_data.freq = float(qso_data.freq)
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue
                else:
                    break
            else:
                break

        while True:
            qso_data.tx_pwr = input('Your power : ')
            if not qso_data.tx_pwr == '':
                try:
                    qso_data.tx_pwr = float(qso_data.tx_pwr)
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue
                else:
                    break
            else:
                break

        while True:
            qso_data.rst_sent = input('Your RST : ')
            if not qso_data.rst_sent == '':
                try:
                    qso_data.rst_sent = int(qso_data.rst_sent)
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue
                if qso_data.rst_sent > 599:
                    print('RST can not be greater than 599.')
                else:
                    break
            else:
                break

        while True:
            qso_data.rx_pwr = input('OM\'s power : ')
            if not qso_data.rx_pwr == '':
                try:
                    qso_data.rx_pwr = float(qso_data.rx_pwr)
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue
                else:
                    break
            else:
                break

        while True:
            qso_data.rst_rcvd = input('OM\'s RST : ')
            if not qso_data.rst_rcvd == '':
                try:
                    qso_data.rst_rcvd = int(qso_data.rst_rcvd)
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue
                if qso_data.rst_rcvd > 599:
                    print('RST can not be greater than 599.')
                else:
                    break
            else:
                break

        qso_data.prop_mode = input('Propagation Mode : ')
        qso_data.qslmeg = input('QSL Message : ')
        qso_data.notes = input('Comments : ')
        
    except(EOFError, KeyboardInterrupt):
        print('\nUser input cancelled. Database not changed. Aborting...')
        return
    # -----

    qso_data.create_db()
    qso_data.insert_into_db()
    log.info('Following record was written in DB :\n {}'.format(qso_data))
    qso_data.close_db()
    return


def main():
    scriptname = 'dolphinlog'
    home_folder = os.path.expanduser('~') + '/.{}/'.format(scriptname)
    default_db_filename = home_folder + '{}.sqlite'.format(scriptname)

    parser = argparse.ArgumentParser()
    parser.add_argument('-db', '--dbfilename', nargs='?', type=str, help='Name of the database file.',
                        default=default_db_filename)
    parser.add_argument('-adi', '--adifilename', nargs='?', type=str, help='Name of the ADIF-ADI file.')
    parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')
    parser.add_argument('--version', help='Print version', action='store_true')

    args = parser.parse_args()

    if args.verbose:
        log.basicConfig(level=log.DEBUG)

    if args.version:
        print('{} {}'.format(scriptname, __version__))
        sys.exit()

    db_fn = args.dbfilename
    if db_fn == default_db_filename:
        log.info('Using the default filename in user\'s home foler.')
        if not os.path.exists(home_folder):
            os.mkdir(home_folder)
    if not db_fn.lower().endswith('.sqlite'):
        db_fn += '.sqlite'

    # check if user likes to export only
    if args.adifilename:
        adi_fn = args.adifilename
        if not adi_fn.lower().endswith('.adi'):
            adi_fn += '.adi'
        QSOData.export_adif_adi(db_fn, adi_fn)
        sys.exit()

    #otherwise start the usual routine

    qso_data = QSOData(db_fn)
    fill_in_data(qso_data)


# ------------------

if __name__ == '__main__':
    main()
