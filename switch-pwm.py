#-*-coding:utf-8-*-
import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.BOARD)
    
    SW = 7
    LED = 11
    
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    
    # 7번 핀을 입력으로 설정.
    GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    try:
        while True:
            # 스위치 상태 판별.
            key_in = GPIO.input(SW)
            
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


if __name__ == "__main__":
    main()