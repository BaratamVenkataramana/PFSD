import pytz
from _datetime import datetime
time1 = pytz.timezone('Asia/Kolkata')
print("Current Time is : ", datetime.now(time1))