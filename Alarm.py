import random
from datetime import datetime, time
import time as t
import winsound

alarminput = input('Uhrzeit (00:00)') or "00:00:00"
alarm = time.fromisoformat(alarminput)
print(alarm)
do = ['push-ups','sit-ups','jumpingjacks']
dordm = random.randint(0,2)
amt = random.randint(10,30)

def getTime():
      Time = datetime.now()
      print(Time)
      return Time


def Task():
        print(Time.time())
        print(f'Do {amt} {do[dordm]}')
        for i in range(100):
            sos()
            t.sleep(1)   


def sos():      
    for i in range(0, 3):              
        winsound.Beep(2000, 100)      
    for i in range(0, 3):              
        winsound.Beep(2000, 400)      
    for i in range(0, 3):              
        winsound.Beep(2000, 100)

for i in range(100):
    Time = getTime()

    if Time.hour == alarm.hour and Time.minute == alarm.minute:
          Task()
     
    t.sleep(60)   
 #       Task()

    #if Time == 1000:
    getTime()



