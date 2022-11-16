pun = 25
kol = 8
rohe = 7
nupp = 21
jp = 16
jr = 20
js = 18

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
nupp_vajutatud = False
GPIO.setup(pun, GPIO.OUT)
GPIO.setup(kol, GPIO.OUT)
GPIO.setup(rohe, GPIO.OUT)
GPIO.setup(jp, GPIO.OUT)
GPIO.setup(jr, GPIO.OUT)
GPIO.setup(js, GPIO.OUT)
GPIO.setup(nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_vajutatud(nupp, js):
    global nupp_vajutatud
    if GPIO.input(21) == GPIO.LOW:
        nupp_vajutatud = True
        GPIO.output(js, True)
        print('tuli siia')
    else:
        print('test')


def pollimine(sekundid):
    sekundid = sekundid * 10
    for i in range(int(sekundid)):
        time.sleep(0.1)
        button_vajutatud(21, js)



GPIO.output(pun, False)
GPIO.output(kol, False)
GPIO.output(rohe, False)
GPIO.output(jp, True)

try:
    while True:      

        
        GPIO.output (rohe, True)
        
        pollimine(5)
        GPIO.output (rohe, False)
        GPIO.output (kol, True)
        
        pollimine(1)

        GPIO.output (kol, False)
        GPIO.output (pun, True)
        if nupp_vajutatud == True:
            GPIO.output(jp, False)
            GPIO.output(jr, True)
            time.sleep(5)
            GPIO.output(jr,False)
            GPIO.output(jp, True)
            GPIO.output(js, False)
            nupp_vajutatud = False
        else:

            pollimine(5)
        

        GPIO.output (pun, False)
        GPIO.output (kol, True)
        
        pollimine(0.3)      
        GPIO.output(kol, False)
        
        pollimine(0.4)
        
        GPIO.output(kol, True)
        
        pollimine(0.3)
        
        
        GPIO.output(kol, False)
        
        pollimine(0.4)
        GPIO.output (kol, True)
        
        pollimine(0.3)
        GPIO.output(kol, False)
        
        pollimine(0.4)

except KeyboardInterrupt:
    print("Keyboard interrupt")
finally:
    GPIO.cleanup()



