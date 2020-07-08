import datetime
import time
print (datetime.datetime.today().strftime("%H"))
print(datetime.datetime.today().strftime("%M"))
hour=int(input("Enter a Hour in (24 hour format): "))
minute=int(input("Enter a Minute: "))
while True:
    print("Checking time now ",datetime.datetime.now())
    if hour == int(datetime.datetime.today().strftime("%H")) and minute == int(datetime.datetime.today().strftime("%M")):
        print("Alarm Raised")
        
        break
    else:
        print("not the correct time..")
        time.sleep(60)