import machine, ssd1306, gfx
import bitmapfont


i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5), freq=100000)
oled = ssd1306.SSD1306_I2C(128,32, i2c)

graphics = gfx.GFX(128, 32, oled.pixel)
#bf = bitmapfont.BitmapFont(128, 32, oled.pixel)
#bf.init()

oled.fill(0)
oled.show()
graphics.line(0, 0, 127, 23, 1)
graphics.rect(0, 0, 120, 30, 1)
graphics.fill_rect(0, 0, 40, 30, 1)
graphics.circle(60, 16, 15, 1)
graphics.fill_circle(60, 16, 10, 1)
graphics.triangle(60, 10, 100, 25, 20, 25, 1)
graphics.fill_triangle(60, 10, 80, 25, 40, 25, 1)
#bf.text('Ada', 0, 0, 100)

oled.show()
