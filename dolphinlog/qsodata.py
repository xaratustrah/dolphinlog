"""
Yet another HAM radio logger using SQLite.

Dec 2015 - xaratustra

"""

import sqlite3
import logging as log
import datetime


class QSOData(object):
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

        self.qso_date = None
        self.time_on = None
        self.call = None
        self.mode = None
        self.band = None
        self.freq = None
        self.prop_mode = None
        self.programid = 'dolphinlog'
        self.qslmeg = None
        self.rst_sent = None
        self.name = None
        self.rst_rcvd = None
        self.rx_pwr = None
        self.tx_pwr = None
        self.gridsquare = None
        self.notes = None

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(self.qso_date,
                                                                        self.time_on,
                                                                        self.call,
                                                                        self.mode,
                                                                        self.band,
                                                                        self.freq,
                                                                        self.prop_mode,
                                                                        self.programid,
                                                                        self.qslmeg,
                                                                        self.rst_sent,
                                                                        self.name,
                                                                        self.rst_rcvd,
                                                                        self.rx_pwr,
                                                                        self.tx_pwr,
                                                                        self.gridsquare,
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
                                qso_date TEXT,
                                time_on	TEXT,
                                call TEXT,
                                mode TEXT,
                                band TEXT,
                                freq REAL,
                                prop_mode TEXT,
                                programid TEXT,
                                qslmeg TEXT,
                                rst_sent INTEGER,
                                name TEXT,
                                rst_rcvd INTEGER,
                                rx_pwr REAL,
                                tx_pwr REAL,
                                gridsquare TEXT,
                                notes TEXT
                                )''')

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
                '''INSERT INTO qso(
                qso_date,
                time_on,
                call,
                mode,
                band,
                freq,
                prop_mode,
                programid,
                qslmeg,
                rst_sent,
                name,
                rst_rcvd,
                rx_pwr,
                tx_pwr,
                gridsquare,
                notes)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (self.qso_date,
                 self.time_on,
                 self.call,
                 self.mode,
                 self.band,
                 self.freq,
                 self.prop_mode,
                 self.programid,
                 self.qslmeg,
                 self.rst_sent,
                 self.name,
                 self.rst_rcvd,
                 self.rx_pwr,
                 self.tx_pwr,
                 self.gridsquare,
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

    @staticmethod
    def export_adif_adi(db_filename, adi_filename):
        try:
            ADIF_VER = '3.0.4'
            PROG_ID = 'dolphinlog'
            log.info('Connecting to database: {}'.format(db_filename))
            db = sqlite3.connect(db_filename)
            cursor = db.cursor()
            cursor.execute('SELECT * FROM qso ORDER BY id')
            names = list(map(lambda x: x[0], cursor.description))
            dat = datetime.datetime.utcnow()
            f = open(adi_filename, 'w')
            f.write('Generated on {} at {} UTC\n\n'.format(dat.strftime('%Y-%m-%d'), dat.strftime('%H:%M:%S')))
            f.write('<adif_ver:{}:>{}\n'.format(len(ADIF_VER), ADIF_VER))
            f.write('<programid:{}:>{}\n'.format(len(PROG_ID), PROG_ID))
            f.write('<eoh>\n\n')
            for row in cursor:
                for i in range(len(row)):
                    if names[i] == 'id' or names[i] == 'programid':
                        continue
                    if str(row[i]) == '':
                        continue
                    f.write('<{}:{}:>{}\n'.format(names[i], len(str(row[i])), str(row[i])))
                f.write('<eor>\n\n')
            f.close()
        except Exception as e:
            # Roll back any change if something goes wrong
            db.rollback()
            log.error('Something wrong.')
            raise e
        finally:
            # Close the db connection
            db.close()

    def export_adif_adx(self):
        pass
