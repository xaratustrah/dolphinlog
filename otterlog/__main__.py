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
from version import __version__
from logdata import LogData

def main():
    scriptname = __file__.split('/')[1].split('.')[0]
    home_folder = os.path.expanduser('~') + '/.{}/'.format(scriptname)
    default_db_filename = home_folder + '{}.sqlite'.format(scriptname)

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', nargs='?', type=str, help='Name of the database file.',
                        default=default_db_filename)
    parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')
    parser.add_argument('--version', help='Print version', action='store_true')

    args = parser.parse_args()

    if args.version:
        print('{} {}'.format(scriptname, __version__))
        sys.exit()

    if args.verbose:
        log.basicConfig(level=log.DEBUG)

    fn = args.filename

    if fn == default_db_filename:
        log.info('Using the default filename in user\'s home foler.')
        if not os.path.exists(home_folder):
            os.mkdir(home_folder)

    # make sure the file extension is correct
    if not fn.lower().endswith('.sqlite'):
        fn += '.sqlite'

    log_data = LogData(filename=fn)

    log_data.qso_date = input('UTC Date YYYYMMDD [empty for today]: ')
    if log_data.qso_date == '':
        log_data.qso_date = datetime.datetime.utcnow().strftime('%Y%m%d')
    log_data.time_on = input('UTC time HHMM [empty for just now]: ')
    if log_data.time_on == '':
        log_data.time_on = datetime.datetime.utcnow().strftime('%H%M')
    log_data.call = input('OM\'s call sign: ')
    log_data.name = input('OM\'s name : ')
    log_data.gridsquare = input('OM\'s locator : ')
    log_data.mode = input('Mode : ')
    log_data.band = input('Band : ')

    while True:
        log_data.freq = input('Frequncy : ')
        if not log_data.freq == '':
            try:
                log_data.freq = float(log_data.freq)
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        else:
            break

    while True:
        log_data.tx_pwr = input('Your power : ')
        if not log_data.tx_pwr == '':
            try:
                log_data.tx_pwr = float(log_data.tx_pwr)
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        else:
            break

    while True:
        log_data.rst_sent = input('Your RST : ')
        if not log_data.rst_sent == '':
            try:
                log_data.rst_sent = int(log_data.rst_sent)
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if log_data.rst_sent > 599:
                print('RST can not be greater than 599.')
            else:
                break
        else:
            break

    while True:
        log_data.rx_pwr = input('OM\'s power : ')
        if not log_data.rx_pwr == '':
            try:
                log_data.rx_pwr = float(log_data.rx_pwr)
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        else:
            break

    while True:
        log_data.rst_rcvd = input('OM\'s RST : ')
        if not log_data.rst_rcvd == '':
            try:
                log_data.rst_rcvd = int(log_data.rst_rcvd)
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if log_data.rst_rcvd > 599:
                print('RST can not be greater than 599.')
            else:
                break
        else:
            break

    log_data.prop_mode = input('Propagation Mode : ')
    log_data.qslmeg = input('QSL Message : ')
    log_data.notes = input('Comments : ')

    # -----

    log_data.create_db()
    log_data.insert_into_db()
    log.info('Following record was written in DB :\n {}'.format(log_data))
    log_data.close_db()


# ------------------

if __name__ == '__main__':
    main()
