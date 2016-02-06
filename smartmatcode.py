import mraa
import time


# attach the buzzer to d4
buzzer = mraa.Gpio(4)
buzzer.dir(mraa.DIR_OUT)
buzzer.write(1)
time.sleep(1)
buzzer.write(0)
