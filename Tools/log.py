import os

class Log:

    def __init__(self, logname):
        self.filename = str(logname + ".log")

    def logwrite(self, logtxt):
        file = open (self.filename, "a")
        file.write(logtxt + " \n")
        file.close()

    def readaline(self):
        file = open(self.filename, "r")
        print(file.readline())
        file.close()

    def readfile(self):
        file = open(self.filename, "r")
        print(file.read())
        file.close()
