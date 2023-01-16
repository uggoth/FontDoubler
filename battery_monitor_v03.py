module_name = 'battery_monitor_v02.py'

print (module_name, 'starting')

import FontDoubler_V04 as FontDoubler
from machine import Pin,ADC
import utime

my_lcd = FontDoubler.LCD2()
my_lcd.set_bl_pwm(65535)
qmi8658=FontDoubler.Display.QMI8658()
Vbat= ADC(Pin(29))   
sensor_temp = ADC(4)

my_lcd.fill(my_lcd.black)
highest = 0.0
lowest = 99.0
charged = False

ts = 0     #  total seconds
sslc = 0   #  seconds since last change

while True:
    utime.sleep(1)
    if sslc > 300:
        charged = True
    if not charged:
        my_lcd.scaled("Voltage",35,40,my_lcd.black,my_lcd.yellow,3)
    else:
        my_lcd.scaled("CHARGED",35,40,my_lcd.black,my_lcd.green,3)
    ts += 1
    sslc += 1
    reading = Vbat.read_u16()*3.3/65535*2
    my_lcd.scaled("Now {:.2f}".format(reading),20,80,my_lcd.black,my_lcd.white,3)
    if reading < lowest:
        lowest = reading
        sslc = 0
        my_lcd.scaled("Low {:.2f}".format(lowest),20,110,my_lcd.black,my_lcd.yellow,3)
    if reading > highest:
        highest = reading
        sslc = 0
        my_lcd.scaled("Hi  {:.2f}".format(highest),20,140,my_lcd.black,my_lcd.yellow,3)
    my_lcd.scaled("TS {:>6}".format(ts),40,170,my_lcd.black,my_lcd.white,2)
    my_lcd.scaled("SSLC {:>4}".format(sslc),40,190,my_lcd.black,my_lcd.white,2)
    temperature = 27 - (((sensor_temp.read_u16() * 3.3 / 65535) - 0.706) / 0.001721)
    if temperature < 45:
        background = my_lcd.black
    else:
        background = my_lcd.red
    my_lcd.fill_rect(0,205,240,39,background)
    my_lcd.text("Temp={:.2f}".format(temperature),80,215,my_lcd.white)
    my_lcd.show()
