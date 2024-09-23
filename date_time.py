import datetime
# date = datetime.date(2019, 11, 27)
# print(date)
# print(datetime.date.today())
#
# print(datetime.time(23, 45, 59))
# print(datetime.datetime.now())

# print(datetime.date(2020, 9, 29))
# print(datetime.datetime(2020, 9, 29))
# print(datetime.time(12, 4, 23))


d1 = datetime.date(2020, 9, 29)
d2 = datetime.date(2018, 11, 18)
print(d1-d2)
print(d1, d2)
d1 += datetime.timedelta(hours=48) #days, hours, minutes, seconds
d2 -= datetime.timedelta(minutes=23456)

print(d1, d2)

