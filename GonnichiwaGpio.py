#-*-coding:UTF-8-*-
import RPi.GPIO as GPIO
import time
from SwitchInput import SwitchInput

import traceback

class GonnichiwaGpio:
    def __init__(self, gpioPin_input=7, gpio_led=11, pwmHz=100): 
        # Constructor parameter
        self.GPIO_INPUT = gpioPin_input # 생성자 파라미터
        self.GPIO_LED   = gpio_led
        # pwm SET
        GPIO.setmode(GPIO.BOARD)
        # LED 연결 setup
        GPIO.setup(self.GPIO_LED, GPIO.OUT, initial=GPIO.LOW)
        # 7번GPIO핀 초기설정.
        GPIO.setup(self.GPIO_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.pwm        = GPIO.PWM(self.GPIO_LED, pwmHz)
        self.pwm.start(0)
        # pwm dutyRatio Array
        self.dutyValues = []

    def __gpioCleanup(self): # private method (객체 외부에서 사용할 수 없다.)
        self.pwm.stop()  # pwm stop
        GPIO.cleanup()   # gpio stop

    def __setDutyRatioArray(self, start=0.1, interval=0.1, end=100.0): # ratio param의 default가 0.1
        print('_setDutyRatioArray', str(start), str(interval), str(end))
        # 듀티 ratio 목록 작성 (0.1단위로 ratio 100.0까지 배열 삽입)
        dutyValues = []
        value = start
        while value <= end:
            dutyValues.append(round(value,1)) # 0.1 단위로 소수점 1째자리까지 추가.
            value = value + interval
        
        print(dutyValues)

        return dutyValues

    #def __ledOnSmoothly(self):
        #self.__changeDutyCycle(self.dutyValues)

    #def __ledOffSmoothly(self):
        #self.__changeDutyCycle(self.dutyValues)

    def start(self):
        self.dutyValues = self.__setDutyRatioArray(start=0.1, interval=0.1, end=100.0)

        try:
            while True:
                # 스위치 입력 판별.
                key_in = GPIO.input(self.GPIO_INPUT)
                
                if key_in == SwitchInput.SWITCH_OPEN:
                    # PWM 으로 천천히 켜짐.
                    #self.__ledOnSmoothly()
                    values = self.dutyValues
                    for val in values:
                        self.pwm.ChangeDutyCycle(val)
                        time.sleep(0.01)
                    
                elif key_in == SwitchInput.SWITCH_CLOSE:
                    # PWM 으로 천천히 꺼짐.
                    #self.__ledOffSmoothly()
                    values = self.dutyValues.reverse()
                    for val in values:
                        self.pwm.ChangeDutyCycle(val)
                        time.sleep(0.01)
                
        except BaseException:
            traceback.print_exc()
            print('exception')
            pass
        
        # cleanup GPIO
        self.__gpioCleanup()
