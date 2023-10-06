#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    expression = r'(?P<hour>[0-9]+):(?P<minutes>[0-9]+):(?P<seconds>[0-9]+)(?P<time>[A-Z]+)'
    match = re.search(expression, s)
    hour = int(match.group('hour'))
    minutes = int(match.group('minutes'))
    seconds = int(match.group('seconds'))
    time = match.group('time')

    if time == 'AM':
        if hour == 12:
            hour = '00'
    else:
        if hour != 12:
            hour += 12

    # Always format minutes and seconds with leading zeros
    curr_time = f'{int(hour):02d}:{int(minutes):02d}:{int(seconds):02d}'

    return curr_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
