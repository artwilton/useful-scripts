"""
This script calculates the difference between two timecode entries in seconds, accurate to the microsecond.
Timecode is assumed to be in the following format HH:MM:SS.MICROSECONDS
"""

import datetime

start_time = "HH:MM:SS.microseconds"
end_time = "HH:MM:SS.microseconds"

def calculateDifference(start, end):
    
    def decimalCheck(time):
        if '.' not in time:
            time = time + '.0'
        return time

    start = datetime.datetime.strptime(decimalCheck(start), "%H:%M:%S.%f")
    end = datetime.datetime.strptime(decimalCheck(end), "%H:%M:%S.%f")
    final_time = (end - start).total_seconds()
    
    print (final_time)

calculateDifference(start_time, end_time)