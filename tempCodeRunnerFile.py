import os
import datetime

alarmHour = int(input("what hour is you want to wake up"))
alarmMinute = int(input("what minute do you want towake up?"))
ampm = str(input("am or pm"))
os.system('cleart')
print("waiting for alarm", alarmHour, alarmMinute, ampm)
if(ampm == "pm"):
    alarmHour = alarmHour + 12
while(1 == 1):
    if(alarmHour == datetime.datetime.now().hour and 
       alarmMinute == datetime.datetime.now().minute):
      print("wake up  lazy")
      #playsound('Users/jae/Music/_Serato_/beep-07.mp3')
    break
print("exited")