import time
import pyupm_i2clcd

RET_ERROR = -1

if __name__ == '__main__':
    lcd = pyupm_i2clcd.Jhd1313m1(6, 0x3E, 0x62)
    with open('/dev/ttymcu0', 'w+t') as f:
        while True:
            f.write('get_distance\n') # Send command to MCU
            f.flush()
            line = f.readline() # Read response from MCU, -1 = ERROR
            value = int(line.strip('\n\r\t '))
            lcd.clear()
            if value == RET_ERROR:
                lcd.setColor(255, 0, 0) # RED
                lcd.write('ERROR')
            else:
                lcd.setColor(0, 255, 0) # GREEN
                lcd.write('%d cm' % (value,))
            time.sleep(1)
