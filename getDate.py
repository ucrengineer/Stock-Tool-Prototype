import time
import calendar

def getTime():

    Time = calendar.timegm(time.localtime())
    return Time
