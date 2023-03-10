module_name = 'FontDoubler_V04.py'

import RP2040_LCD_CLOCK_V02 as Display

class LCD2(Display.LCD_1inch28):
    def __init__(self):
        super().__init__()
        self.base_font_width = 8
        self.base_font_height = 8
        self.max_scale = 8
        self.max_characters = 20
        self.work_height = self.base_font_height
        self.work_width = self.base_font_width * self.max_characters
        self.work_buffer = bytearray(self.work_height * self.work_width * 2)
        self.work_area = Display.framebuf.FrameBuffer(self.work_buffer,
                        self.work_width, self.work_height, Display.framebuf.RGB565)
        self.red    =  0x07e0
        self.green  =  0x001f
        self.yellow =  0x07ff
        self.blue   =  0xf800
        self.purple =  0xffe0
        self.white  =  0xffff
        self.black  =  0x0000
    def scaled(self, text, x, y, background, foreground, scale=1, padding=0):
        result = 0
        w = len(text)
        if w > self.max_characters:
            result = 40
            w = self.max_characters
        if w < 1:
            return 50
        s = scale
        if s > self.max_scale:
            s = self.max_scale
            result = 20
        if s < 1:
            s = 1
            result = 30
        rect_width = w * self.base_font_width * s
        rect_height = self.base_font_height * s
        self.work_area.fill_rect(0,0,rect_width,rect_height,background)
        self.work_area.text(text,0,0,foreground)
        if padding > 0:
            self.fill_rect(x, y-padding, rect_width, padding, background)
        width = w * self.base_font_width
        for i in range(width):
            x2 = i
            x3 = x + (i * s)
            for j in range(self.work_height):
                y2 = j
                y3 = y + (j * s)
                c = self.work_area.pixel(x2,y2)
                if c is None:
                    c = self.blue
                self.fill_rect(x3,y3,s,s,c)
        self.show()
        return result

if __name__ == '__main__':
    print (module_name, 'starting')
    my_lcd = LCD2()
    my_lcd.fill(my_lcd.black)
    print (my_lcd.scaled('Colin',35,40,my_lcd.black,my_lcd.yellow,4,3))
    print (my_lcd.scaled('Walls',35,80,my_lcd.black,my_lcd.yellow,4,3))
    print (my_lcd.scaled('Sidmouth',20,140,my_lcd.black,my_lcd.red,3,3))
    print (my_lcd.scaled('Robots',40,170,my_lcd.black,my_lcd.red,3,3))
    print (module_name, 'finished')
