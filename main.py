module_name = 'test_21_B_display.py'

import RP2040_LCD_CLOCK_V01 as Display
import utime

print (module_name, 'starting')

LCD = Display.LCD_1inch28()
LCD.set_bl_pwm(65535)
qmi8658=Display.QMI8658()
Vbat= Display.ADC(Display.Pin(Display.Vbat_Pin))   

LCD.fill(LCD.white)

LCD.fill_rect(0,0,240,80,LCD.red)
LCD.text("Colin",80,25,LCD.white)
LCD.text("Walls",100,57,LCD.white)

LCD.fill_rect(0,80,240,120,LCD.blue)

#LCD.poly(20,200,[0,0,0,20,20,40,25,20,0,0],LCD.white,True)
#LCD.fill_ellipse(22,22)
LCD.line(20,120,50,200,LCD.white)

while True:
    LCD.fill_rect(0,120,240,140,LCD.blue)
    reading = Vbat.read_u16()*3.3/65535*2
    LCD.text("Vbat = {:.2f}".format(reading),80,200,LCD.white)
    LCD.show()
    utime.sleep_ms(100)

utime.sleep(5)

print (module_name, 'finished')
