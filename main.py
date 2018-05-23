#!/usr/bin/env python
import os
import time
from merge import merge
from clientReport import getClientReport
from getToggleReport import getToggleReport
from getAnalyticsReport import getAnalyticReport
from fileSystem import FileSystem


class Site():
    def __init__(self, name, manageWpDiv, togglID):
        self.name = name
        self.manageWpDiv = manageWpDiv
        self.togglID = togglID

    def createMainFolder(self):
        fileSystem = FileSystem(self.name)
        fileSystem.createMainFolder()

    def createMonthFolder(self):
        fileSystem = FileSystem(self.name)
        fileSystem.createMonthFolder()

    def renameAndMoveFile(self, filename):
        fileSystem = FileSystem(self.name)
        fileSystem.renameAndMoveFile(filename)

    def clientReport(self):
        # Get The Client Report
        getClientReport(self.name)
        # Wait 5 Seconds
        time.sleep(5)
        # Rename The File And Move It
        self.renameAndMoveFile('Client Report.pdf')

    def togglReport(self):
        # Get The Toggl Report
        getToggleReport(self.togglID)
        # Rename The File And Move It
        self.renameAndMoveFile('Content Updates.pdf')

    def createReports(self):
        self.createMainFolder()
        self.createMonthFolder()
        self.clientReport()
        self.togglReport()

    def mergePDFs(self):
        merge(self.name)


jst = Site(
    "Justin Sports Medicine Team",
    "JustinSport",
    "40727730"
)
bbs = Site(
    'Beautiful Bennett Sphynx',
    'BEAUTIFUL BENNETT SPHYNX',
    '54422761'
)


def createReports():
    jst.createReports()
    bbs.createReports()


def mergeReports():
    jst.mergePDFs()
    bbs.mergePDFs()


def main():
    os.system('clear')
    print('')
    print('1: Create Folders and Reports')
    print('2: Merge Folders')
    print('')
    print('')
    choice = input('Please Choose An Option: ')
    print('User Chose: {}').format(choice)
    if choice == 1:
        print('Creating Reports....')
        createReports()
        print('Finished')
    elif choice == 2:
        mergeReports()
    else:
        print('You Must Enter Either 1 Or Two')
        main()


main()
