#-*-coding:UTF-8-*-
import RPi.GPIO as GPIO
from SwitchInput import SwitchInput

class GonnichiwaGpio:
    def __init__(self): # 
        self.num = 0    # Î©§Î≤Ñ Î≥Ä?? 'self' ?ÑÏàò

    def getNum(self): # ?úÌóò??        num = self.num
        return num

    def start(self):
        GPIO.setmode(GPIO.BOARD)
    
        GPIOPIN_7 = 7
        LED = 11
        
        GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
        
        # 7Î≤??Ä???ÖÎ†•?ºÎ°ú ?§Ï†ï.
        GPIO.setup(GPIOPIN_7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        try:
            while True:
                # ?§ÏúÑÏπ??ÅÌÉú ?êÎ≥Ñ.
                key_in = GPIO.input(GPIOPIN_7)
                
                if key_in == 0:
                    print('gpio.high')
                    GPIO.output(LED, GPIO.HIGH)
                else:
                    print('gpio.low')
                    GPIO.output(LED, GPIO.LOW)
                
        except BaseException:
            print('exception')
            pass
        
        GPIO.cleanup()
