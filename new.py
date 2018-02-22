import  RPi.GPIO as GPIO
import time


'''GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)'''

'''GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
p=' '
pp=' '
while True:
    if(GPIO.input(17)==1)and(GPIO.input(27)==1):
        p=p+'a'   
        #print("a",end='')
    elif(GPIO.input(27)==1)and(GPIO.input(22)==1):
        p=p+'b' 
        #print("b",end='')
    elif(GPIO.input(22)==1)and(GPIO.input(23)==1):
        p=p+'c' 
        #print("c",end='')

    else:
        #print("Invalid")
        pp=p
        print(pp)
        #fun(pp)
        
    time.sleep(0.5)

