"""
This script calculates the difference between two timecode entries in microseconds.
Timecode is assumed to be in the following format HH:MM:SS.MICROSECONDS
"""

start_time = "HH:MM:SS.MICROSECONDS"
end_time = "HH:MM:SS.MICROSECONDS"

calculateDifference(start, end):
    
    def decimalCheck(time):
        if '.' not in time:
            time = time + '.0'
        return time

    start = datetime.datetime.strptime(decimalCheck(start), "%H:%M:%S.%f")
    end = datetime.datetime.strptime(decimalCheck(end), "%H:%M:%S.%f")
    return (end - start).microseconds/1000000