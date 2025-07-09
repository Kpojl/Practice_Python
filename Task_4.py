import math
import time
import datetime
from datetime import timedelta

sec = int(input("Ввседите колличество секунд:"))

days = sec // 86400 
hours = sec % 86400 // 3600 
minutes = sec % 3600 // 60 
seconds = sec % 60 

print()