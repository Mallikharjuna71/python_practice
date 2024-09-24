from datetime import datetime
# date = datetime.date(2019, 11, 27)
# print(date)
# print(datetime.date.today())
#
# print(datetime.time(23, 45, 59))
# print(datetime.datetime.now())

# print(datetime.date(2020, 9, 29))
# print(datetime.datetime(2020, 9, 29))
# print(datetime.time(12, 4, 23))


# d1 = datetime.date(2020, 9, 29)
# d2 = datetime.date(2018, 11, 18)
# print(d1-d2)
# print(d1, d2)
# d1 += datetime.timedelta(hours=48) #days, hours, minutes, seconds
# d2 -= datetime.timedelta(minutes=23456)
#
# print(d1, d2)
# format = '%a %d %b %Y %H:%M:%S %z'
#
# d = 'Sun 10 May 2015 13:54:36 -0700'
# d1 = 'Sun 10 May 2015 13:54:36 -0000'
# def time_delta(date1, date2):
#     date = datetime.strptime(d, format)
#     date1 = datetime.strptime(d1, format)
#     print(str(int((date-date1).total_seconds())))
#
import numpy
numpy.set_printoptions(legacy='1.13')

def floor_ceil_rint(n):
    my_array = numpy.array(n)
    print(numpy.floor(my_array))
    print(numpy.ceil(my_array))
    print(numpy.rint(my_array))

n = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
floor_ceil_rint(n)