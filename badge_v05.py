module_name = 'badge_v05.py'

print (module_name, 'starting')

import FontDoubler_V04 as FontDoubler
from machine import Pin,ADC
import utime

my_lcd = FontDoubler.LCD2()
my_lcd.set_bl_pwm(65535)
qmi8658=FontDoubler.Display.QMI8658()
Vbat= ADC(Pin(29))   

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

my_lcd.fill(my_lcd.black)
my_lcd.scaled('Colin',35,40,my_lcd.black,my_lcd.yellow,4,3)
my_lcd.scaled('Walls',35,80,my_lcd.black,my_lcd.yellow,4,3)

min_greenness = 0
max_greenness = 64
base_red = 0x07e0
current_greenness = 0
direction = 1

while True:
    utime.sleep_ms(200)
    this_red = base_red + current_greenness
    current_greenness += direction
    if current_greenness >= max_greenness:
        direction = -1
        print ('going down')
    if current_greenness <= min_greenness:
        direction = 1
        print ('going up')
    my_lcd.scaled('Sidmouth',20,135,my_lcd.black, this_red,3,3)
    my_lcd.scaled('Robots',40,165,my_lcd.black, this_red,3,3)
    my_lcd.fill_rect(0,200,240,30,my_lcd.black)
    volts = Vbat.read_u16()*3.3/65535*2
    my_lcd.text("Vbat={:.2f}".format(volts),80,205,my_lcd.white)
    temp = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (temp - 0.706)/0.001721
    my_lcd.text("Temp={:.2f}".format(temperature),75,220,my_lcd.white)
    my_lcd.show()
    if volts < 3.2:
        my_lcd.fill(my_lcd.black)
        my_lcd.scaled('Low',65,50,my_lcd.black,my_lcd.yellow,4,3)
        my_lcd.scaled('Battery',15,110,my_lcd.black,my_lcd.yellow,4,3)
        utime.sleep(240)
        my_lcd.fill(my_lcd.black)
        my_lcd.show()
        break
    if temp > 45:
        my_lcd.fill(my_lcd.black)
        my_lcd.scaled('Too',65,50,my_lcd.black,my_lcd.yellow,4,3)
        my_lcd.scaled('Hot',15,110,my_lcd.black,my_lcd.yellow,4,3)
        utime.sleep(240)
        my_lcd.fill(my_lcd.black)
        my_lcd.show()
        break


print (module_name, 'finished')