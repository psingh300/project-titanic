import mraa
import time

B=4275
R0=100000

#tempcode
temp = mraa.Aio(0)
temp.read()
R = 1023/temp.readFloat()-1.0
R =R0*R
tempC=1.0/(log(R/100000.0)/B+1/298.15)-273.15;
print (tempC)


# buzzer code
buzzer = mraa.Gpio(4)
buzzer.dir(mraa.DIR_OUT)
buzzer.write(1)
time.sleep(1)
buzzer.write(0)
