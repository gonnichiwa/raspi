import RPi.GPIO as GPIO
from SwitchInput import SwitchInput

class GonnichiwaGpio:
    def __init__(self): # 
        self.num = 0    # 멤버 변수. 'self' 필수

    def getNum(self): # 시험용
        num = self.num
        return num

    def start(self):
        GPIO.setmode(GPIO.BOARD)
    
        GPIOPIN_7 = 7
        LED = 11
        
        GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
        
        # 7번 핀을 입력으로 설정.
        GPIO.setup(GPIOPIN_7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        try:
            while True:
                # 스위치 상태 판별.
                key_in = GPIO.input(GPIOPIN_7)
                
                if key_in == SwitchInput.FALSE:
                    print('gpio.high')
                    GPIO.output(LED, GPIO.HIGH)
                elif key_in == SwitchInput.TRUE:
                    print('gpio.low')
                    GPIO.output(LED, GPIO.LOW)
                
        except BaseException:
            print('exception')
            pass
        
        GPIO.cleanup()
