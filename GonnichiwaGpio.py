#-*-coding:UTF-8-*-
import RPi.GPIO as GPIO
import time
from SwitchInput import SwitchInput

class GonnichiwaGpio:
    def __init__(self): 
        self.num = 0    

    def getNum(self):
        return self.num

    def start(self):
        GPIO.setmode(GPIO.BOARD)
    
        GPIOPIN_7 = 7
        LED = 11
        
        # LED 연결 setup
        GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
        # 7번GPIO핀 초기설정.
        GPIO.setup(GPIOPIN_7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        try:
            while True:
                # 스위치 입력 판별.
                key_in = GPIO.input(GPIOPIN_7)
                
                if key_in == SwitchInput.SWITCH_OPEN:
                    print('gpio.high')
                    GPIO.output(LED, GPIO.HIGH)
                else:
                    print('gpio.low')
                    GPIO.output(LED, GPIO.LOW)
                
        except BaseException:
            print('exception')
            pass
        
        GPIO.cleanup()
