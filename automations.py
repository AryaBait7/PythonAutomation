import pywhatkit
from datetime import datetime
now =datetime.now()
curr_time_hr=now.strftime("%H")
curr_time_min=now.strftime("%M")
pywhatkit.sendwhatmsg("+918425880069","Heyy",int(curr_time_hr),int(curr_time_min)+1)
print(curr_time_hr)

print((curr_time_min))
print(int(curr_time_min))