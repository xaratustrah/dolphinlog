#!/usr/bin/env python
"""
Yet another QSO logger for HAMs.

Dec 2015 - xaratustra

"""

import sqlite3
import argparse
import logging as log
import os
import datetime


class LogData(object):
    """
    Class for handling log data
    """

    def __init__(self, filename):
        """
        Initiator of the class
        :param filename:
        :return:
        """
        self.db = None
        self.cursor = None
        self.filename = filename

        # QSO related fields

        self.date = None
        self.time = None
        self.call = None
        self.om = None
        self.qth = None
        self.band = None
        self.mode = None
        self.qro = None
        self.rst = None
        self.notes = None

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.date,
                                                      self.time,
                                                      self.call,
                                                      self.om,
                                                      self.qth,
                                                      self.band,
                                                      self.mode,
                                                      self.qro,
                                                      self.rst,
                                                      self.notes)

    def create_db(self):
        """
        Create the database.
        :return:
        """
        try:
            # Creates or opens a file with a SQLite3 DB
            self.db = sqlite3.connect(self.filename)
            # Get a cursor object
            self.cursor = self.db.cursor()
            # Check if table users does not exist and create it
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                          qso(id INTEGER PRIMARY KEY AUTOINCREMENT,
                          date TEXT,
                          time TEXT,
                          call TEXT,
                          om TEXT,
                          qth TEXT,
                          band TEXT,
                          mode TEXT,
                          qro REAL,
                          rst INTEGER,
                          notes TEXT,
                          relatedtoqso INTEGER)''')

            # Commit the change
            self.db.commit()
            log.info('DB creation successful.')

        # Catch the exception
        except Exception as e:
            # Roll back any change if something goes wrong
            self.db.rollback()
            log.error('Something wrong.')
            raise e
            # finally:
            #     # Close the db connection
            #     self.db.close()

    def insert_into_db(self):
        """
        Insert a new entry into the database
        :return:
        """
        try:
            self.cursor.execute(
                'INSERT INTO qso(date, time, call, om, qth, band, mode, qro, rst, notes) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (self.date,
                 self.time,
                 self.call,
                 self.om,
                 self.qth,
                 self.band,
                 self.mode,
                 self.qro,
                 self.rst,
                 self.notes))
            # Commit the change
            self.db.commit()
            log.info('DB commit successful.')
        # Catch the exception
        except Exception as e:
            # Roll back any change if something goes wrong
            self.db.rollback()
            log.error('Something wrong.')
            raise e

    def close_db(self):
        # Close the db connection
        self.db.close()


# ------------ MAIN ----------------------------

__version_info__ = (0, 9, 0)
__version__ = '.'.join('%d' % d for d in __version_info__)
verbose = False

if __name__ == '__main__':

    scriptname = __file__.split('/')[1].split('.')[0]
    home_folder = os.path.expanduser('~') + '/.{}/'.format(scriptname)
    default_db_filename = home_folder + '{}.sqlite'.format(scriptname)

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', nargs='?', type=str, help='Name of the database file.',
                        default=default_db_filename)
    parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')

    args = parser.parse_args()
    if args.verbose:
        log.basicConfig(level=log.DEBUG)
        verbose = True

    fn = args.filename

    if fn == default_db_filename:
        log.info('Using the default filename in user\'s home foler.')
        if not os.path.exists(home_folder):
            os.mkdir(home_folder)

    # make sure the file extension is correct
    if not fn.lower().endswith('.sqlite'):
        fn += '.sqlite'

    log_data = LogData(filename=fn)

    log_data.date = input('Local date YY-MM-DD [empty for today]: ')
    if log_data.date == '':
        log_data.date = datetime.datetime.now().strftime('%Y-%m-%d')
    log_data.time = input('Local time HH:MM [empty for just now]: ')
    if log_data.time == '':
        log_data.time = datetime.datetime.now().strftime('%H:%M')
    log_data.call = input('OM\'s call sign: ')
    log_data.om = input('OM\'s name: ')
    log_data.qth = input('OM\'s QTH: ')
    log_data.band = input('Band : ')
    log_data.mode = input('Mode : ')

    while True:
        log_data.qro = input('Your power [W] : ')
        if not log_data.qro == '':
            try:
                log_data.qro = float(log_data.qro)
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        else:
            break

    while True:
        log_data.rst = input('OM\'s RST : ')
        if not log_data.rst == '':
            try:
                log_data.rst = int(log_data.rst)
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if log_data.rst > 599:
                print('RST can not be greater than 599.')
            else:
                break
        else:
            break

    log_data.notes = input('Any other comments? : ')

    log_data.create_db()
    log_data.insert_into_db()
    log.info('Following record was written in DB :\n {}'.format(log_data))
    log_data.close_db()
