"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input:
07:05:45PM
Output:
19:05:45
"""


def time_conversion(s):
    time = str(s).split(':')
    time_last = time[-1]
    hour = str(time[0])
    min = str(time[1])
    sec = str(time_last[:2])
    if time_last[-2:] == 'PM':
        if hour == '12':
            print(hour+':'+min+':'+sec)
        elif int(hour) < 12:
            hour = str(int(time[0]) + 12)
            if hour == '24' and int(min) > 0 and int(sec) > 0:
                hour = '00'
                print(hour+':'+min+':'+sec)
            else:
                print(hour + ':' + min + ':' + sec)
    else:
        if int(hour) < 12:
            print(hour+':'+min+':'+sec)
        else:
            print('00'+':'+min+':'+sec)


time_conversion('07:05:45PM')
time_conversion('12:40:22AM')
time_conversion('06:40:03AM')
time_conversion('06:45:54PM')
time_conversion('11:45:54AM')
time_conversion('04:59:59AM')
time_conversion('11:45:54PM')
time_conversion('12:45:54PM')
time_conversion('12:00:01PM')
