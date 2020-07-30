#-*-coding:utf-8-*-
from GonnichiwaGpio import GonnichiwaGpio

def main():
    gonGpio = GonnichiwaGpio()
    gonGpio.getNum() # method 출력 테스트 용
    gonGpio.start()


if __name__ == "__main__":
    main()