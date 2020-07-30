#-*-coding:UTF-8-*-
import RPi.GPIO as GPIO
import time
from SwitchInput import SwitchInput

class GonnichiwaGpio:
    def __init__(self, gpioPin_input, gpio_led, pwmHz=100): 
        # Constructor parameter
        self.GPIO_INPUT = gpioPin_input # 생성자 파라미터
        self.GPIO_LED   = gpio_led
        # pwm SET
        GPIO.setmode(GPIO.BOARD)
        self.pwm        = GPIO.PWM(self.GPIO_LED, pwmHz)
        self.pwm.start(0)
        # pwm dutyRatio Array
        self.dutyValues = []

    def __gpioCleanup(self): # private method (객체 외부에서 사용할 수 없다.)
        GPIO.cleanup()

    def __setDutyRatioArray(self, ratio=0.1): # ratio param의 default가 0.1
        # 듀티 비 목록 작성 (0.1단위로 ratio까지 배열 삽입)
        dutyValues = []
        value = ratio
        while value <= 100.0:
            dutyValues.append(round(value,1))
            value = value + 0.1
            
        return dutyValues

    def __changeDutyCycle(self, dutyArr):
        for val in dutyArr:
            self.pwm.ChangeDutyCycle(val)
            time.sleep(0.001)
    
    def __ledOnSmoothly(self):
        dutyValues = self.__setDutyRatioArray(ratio=0.1)
        self.__changeDutyCycle(dutyValues)

    def __ledOffSmoothly(self):
        dutyValues = self.__setDutyRatioArray(ratio=0.1).reverse()
        self.__changeDutyCycle(dutyValues)



    def start(self):
        GPIO.setmode(GPIO.BOARD)
    
        GPIOPIN_7 = self.GPIO_INPUT
        LED = self.GPIO_LED
        
        # LED 연결 setup
        GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
        # 7번GPIO핀 초기설정.
        GPIO.setup(GPIOPIN_7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        try:
            while True:
                # 스위치 입력 판별.
                key_in = GPIO.input(GPIOPIN_7)
                
                if key_in == SwitchInput.SWITCH_OPEN:
                    # TODO: PWM 으로 천천히 켜짐.
                    self.__ledOnSmoothly()
                    #GPIO.output(LED, GPIO.HIGH)
                else:
                    # TODO: PWM 으로 천천히 꺼짐.
                    self.__ledOffSmoothly()
                    #GPIO.output(LED, GPIO.LOW)
                
        except BaseException:
            print('exception')
            pass
        
        # cleanup GPIO
        self.__gpioCleanup()
