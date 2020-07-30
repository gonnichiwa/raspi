#-*-coding:utf-8-*-
from GonnichiwaGpio import GonnichiwaGpio

def main():
    gonGpio = GonnichiwaGpio(gpioPin_input=7, gpio_led=11)
    gonGpio.start()


if __name__ == "__main__":
    main()