import datetime

today =datetime.datetime.now()
print(today)
print(today.strftime("%d/%m/%Y"))

time = today.strftime("%H:%M:%S")
print(time)
