import pyupm_i2clcd as lcd
import time
import pyupm_grove as grove
import sys, signal, atexit
import pyupm_otp538u as upmOtp538u

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
OTP538U_AREF = 5.0
myTempIR = upmOtp538u.OTP538U(0, 1, OTP538U_AREF)
button = grove.GroveButton(0)

def show_temp():
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write(str(myTempIR.objectTemperature()))

def write_welcome():
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write("Welcome      ")

def did_i_ask():
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write("Did I ask")


while True:
    if button.value() == 0:
        write_welcome()
    else:
        show_temp()


del button
