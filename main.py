#!/usr/bin/env python
import time
from clientReport import getClientReport
from getToggleReport import getToggleReport
from getAnalyticsReport import getAnalyticReport
from fileSystem import FileSystem


class Site:
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
        self.renameAndMoveFile('Client Report')

    def togglReport(self):
        # Get The Toggl Report
        getToggleReport(self.togglID)
        # Rename The File And Move It
        self.renameAndMoveFile('Content Updates')

    def analyticsReport(self):
        getAnalyticReport(self.name)


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

jst.analyticsReport()


# # Creates The Main Folder
# bbs.createMainFolder()
# # Creates A Folder For The Current Month
# bbs.createMonthFolder()
# # Downloads The Client Report From Managewp
# bbs.togglReport()
# # Downs The Content UpDates Report From Toggl
# bbs.clientReport()


# # Creates The Main Folder
# jst.createMainFolder()
# # Creates A Folder For The Current Month
# jst.createMonthFolder()
# # Downloads The Client Report From Managewp
# jst.clientReport()
# # Downs The Content UpDates Report From Toggl
# jst.togglReport()
