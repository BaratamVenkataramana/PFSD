import datetime
import time
print(time.time())
# print(time.asctime())
print(time.asctime(time.localtime(time.time())))

datetime_object = datetime.datetime.now()
print(datetime_object)

#print("Year: ", datetime_object.year)
#print("Month: ",datetime_object.month)
#print("Hour: ",datetime_object.hour)
#print("Minute: ",datetime_object.minute)
#print("Second: ",datetime_object.second)


# import calendar
# s= calendar.prcal(2020+2)
#
# import pytz
# UTC = pytz.utc
# print("UTC in Default Format : ",
#       datetime.datetime.now(UTC))
#
# datetime_utc = datetime.now(UTC)
# print("Date & Time in UTC : ",
#       datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))