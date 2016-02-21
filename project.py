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
def write_goodbye():
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write("Goodbye         ")


while True:
    if button.value() == 1:
        print ("debug ...... 1")
        write_welcome()
        print ("debug ...... 2")
        time.sleep(4)
        print ("debug ...... 3")
        while True:
            print ("debug ...... 4")
            show_temp()
            print ("debug ...... 5")
            time.sleep(2)
            print ("debug ......6 ")
            if button.value() == 1:
                print ("debug ...... 7")
                write_goodbye()
                print ("debug ...... 8")
                exit()
