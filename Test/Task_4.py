import math

sec = int(input("Введите количество секунд:"))

days = sec // 86400 
hours = sec % 86400 // 3600 
minutes = sec % 3600 // 60 
seconds = sec % 60 

print("%02d:%02d:%02d:%02d" % (days, hours, minutes, seconds))