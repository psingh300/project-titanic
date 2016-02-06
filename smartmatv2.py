import mraa
import time
import math

#source : http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor#With_Arduino
#source : http://www.seeedstudio.com/wiki/images/8/86/101020015.pdf

bValue=4275
#bValue=4250
THRESHOLD_TEMPERATURE = 10

temp = mraa.Aio(0)

#find average over 20 readings
total_value=0
for index in range(20):
    #sensor_value=temp.read()
    sensor_value=temp.readFloat()
    print("temperature:" + str(sensor_value) )
    #print("float temperature:" + str(temp.readFloat()))
    total_value += sensor_value
    time.sleep(0.5)
average_value = float(total_value/20)
print("Average Temperature:" + str(average_value) )


#convert sensor reading into degree celsius
sensor_value_tmp = (float) (average_value / 4095 * 2.95 * 2 / 3.3 * 1023)
print("sensor_value_tmp="+str(sensor_value_tmp))
resistance = (float) (1023 - sensor_value_tmp) * 100000 / sensor_value_tmp
print("resistance =" + str(resistance))
temperature = round((float)(1 / (math.log(resistance / 100000) / bValue + 1 / 298.15) - 273.15), 2)

print ("Temperature in C = " + str(temperature))
if temperature < THRESHOLD_TEMPERATURE:
    print ("Below Threshold ")
else:
    print ("Above or equal to Threshold")
