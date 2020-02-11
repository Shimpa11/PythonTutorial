import datetime
import datetime as dt
today=dt.datetime.today()
print(today)
print(type(today))

# today=str(dt.datetime.today())
tomorrow=dt.datetime(1985,4,5,12,10,5)
print(tomorrow)
total=today-tomorrow

print(total)