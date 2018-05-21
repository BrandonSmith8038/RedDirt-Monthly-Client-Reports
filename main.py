#!/usr/bin/env python
import time
from clientReport import getClientReport
from fileSystem import FileSystem


class Site:
    def __init__(self, name, manageWpDiv):
        self.name = name
        self.manageWpDiv = manageWpDiv

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
        self.renameAndMoveFile('Client Report')


jst = Site(
    "Justin Sports Medicine Team",
    "JustinSport"
)

# Creates A Folder For The Current Month
# jst.createMonthFolder()
# Downloads The Client Report From Managewp
jst.clientReport()
