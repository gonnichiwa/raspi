#-*-coding:UTF-8-*-
import RPi.GPIO as GPIO
import time

class GonnichiwaGpio:
    def __init__(self): # 
        self.num = 0    # 멤버 변?? 'self' ?�수

    def getNum(self): # ?�험??        num = self.num
        return num

    def start(self):
        GPIO.setmode(GPIO.BOARD)
    
        GPIOPIN_7 = 7
        LED = 11
        
        GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
        
        # 7�??�???�력?�로 ?�정.
        GPIO.setup(GPIOPIN_7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        try:
            while True:
                # ?�위�??�태 ?�별.
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
