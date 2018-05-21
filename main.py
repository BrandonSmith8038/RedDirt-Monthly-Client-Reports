#!/usr/bin/env python
import datetime

from clientReport import getClientReport


class Site:
    def __init__(self, name, folderName, manageWpDiv):
        self.name = name
        self.folderName = folderName
        self.manageWpDiv = manageWpDiv

    def clientReport(self):
        getClientReport(self.name)


jst = Site(
    "Justin Sports Medicine Team",
    "justin sports medicine team",
    "JustinSport"
)

jst.clientReport()
