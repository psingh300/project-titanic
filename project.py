import pyupm_i2clcd as lcd
import time
import pyupm_grove as grove
import sys, signal, atexit
import pyupm_otp538u as upmOtp538u
# ALL VARIABLES BELONG HERE
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
OTP538U_AREF = 5.0
myTempIR = upmOtp538u.OTP538U(0, 1, OTP538U_AREF)
button = grove.GroveButton(0)
# all functions go here
def show_temp():
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write(str(myTempIR.objectTemperature()))

def write_welcome():
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write("Welcome    ")
def write_goodbye():
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write("Goodbye      ")
# Program  is starting from here
write_welcome()
while True:
    if button.value() == 1:
        time.sleep(2)
        while True:
            show_temp()
            time.sleep(2)
            if button.value() == 1:
                write_goodbye()
                exit()
