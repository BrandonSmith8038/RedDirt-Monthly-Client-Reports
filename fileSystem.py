#!/usr/bin/env python
import os
import errno
import datetime

currentMonth = datetime.datetime.now().strftime("%B")


class FileSystem():
    def __init__(self, name):
        self.name = name
        self.mainFolder = '/home/cowboy8038/scripts/Invoices/{}'.format(
            name)
        self.monthFolder = '{}/{}'.format(self.mainFolder, currentMonth)
        self.downloadsFolder = '/home/cowboy8038/Downloads/'

    def createMainFolder(self):
        if not os.path.exists(self.mainFolder):
            try:
                os.makedirs(self.mainFolder, 0o700)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    def createMonthFolder(self):
        if not os.path.exists(self.monthFolder):
            try:
                os.makedirs(self.monthFolder, 0o700)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    def renameAndMoveFile(self, newFileName):
        path = self.downloadsFolder
        filenames = os.listdir(path)
        # os.rename('{}*.pdf'.format(self.downloadsFolder),
        #           '{}.pdf'.format(fileName))
        for filename in filenames:
            os.rename('{}{}'.format(self.downloadsFolder, filename),
                      '{}/{}'.format(self.monthFolder, newFileName))
