import datetime
import pytz

#naive vs aware datetimes

#datetime.date - year month and day
d = datetime.date(2017, 7, 24)
# print d

tday = datetime.date.today()
# print tday
# print tday.year, tday.month, tday.day
# print tday.weekday() # - number of the day of the week - Monday 0 - Sunday 6
# print tday.isoweekday() # - Monday 1 - Sunday 7

#time deltas - difference between dates
tdelta = datetime.timedelta(days=7)
# print tday + tdelta #adding a date and a time delta returns a date
#date2 = date1 + timedelta
#timedelta = date1 + date2

bday = datetime.date(2018, 1, 3)
till_bday = bday - tday
# print till_bday, till_bday.days, till_bday.total_seconds()


#datetime.time - hour, minute, second, microseconds
t = datetime.time(9, 30, 45, 100000)
# print t


#datetime.datetime - year, month, day, hour, minute, second, microseconds
dt = datetime.datetime(2017, 1, 2, 2, 30, 35, 9)
# print dt, dt.date(), dt.time()
# print dt.year

tdelta = datetime.timedelta(hours=23)
# print dt + tdelta

dt_today = datetime.datetime.today() # no timezone
dt_now = datetime.datetime.now() #option to pass in timezone
dt_utcnow = datetime.datetime.utcnow() #still naive

# print dt_today
# print dt_now
# print dt_utcnow


#pytz
#timezone aware datetime using utc
dt = datetime.datetime(2017, 1, 2, 5, 30, 45, tzinfo=pytz.UTC)
# print dt

dt_now = datetime.datetime.now(tz=pytz.UTC)
print dt_now
