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
#LCD to I2C port (leftmost)
# button  goes to UART port
# IR temp sensor goes to A0
#LED goes to D6

def show_temp():
    myLcd.clear()
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    temp_str = str(myTempIR.objectTemperature())
    myLcd.write(temp_str[:5]+"         ")
def write_welcome():
    myLcd.clear()
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write("Welcome       ")
    myLcd.setCursor(1,0)
    myLcd.write("                 ")
def write_goodbye():
    myLcd.clear()
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write("Goodbye          ")
def write_dessert():
    myLcd.clear()
    myLcd.setCursor(0,0)
    myLcd.setColor(233, 201, 223)
    myLcd.write("Would you like             ")
    myLcd.setCursor(1,0)
    myLcd.write("Dessert :) ?             ")

# Program  is starting from here
#starting_temp = myTempIR.objectTemperature()
#dessert_temp = starting_temp - 4
end_temp = 30

while True:
    try:
#        print("SmartMat: Waiting for Button Press")
        if button.value() == 1:
#            print("SmartMat: Recording Temperature")
            write_welcome()
            time.sleep(2)
            while True:
                show_temp()
                time.sleep(2)
                if myTempIR.objectTemperature() < end_temp:
                    write_dessert()
                    break
    except KeyboardInterrupt:
#        print("Bye")
        sys.exit()
