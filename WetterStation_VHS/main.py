import dht
from time import sleep
from bmp180 import BMP180
from machine import Pin, I2C
import ssd1306, time, gfx # , log
from openweathermap import Weather


i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
d = dht.DHT11(Pin(14, Pin.IN, Pin.PULL_UP))
graphics = gfx.GFX(128, 32, oled.pixel)
bmp = BMP180(i2c)
# logging = log.Log("datalog")
# weather = Weather(' API-Key ', ' ORT ')


bmp.oversample_sett = 2
bmp.baseline = 101325


def Oled_dht(Temper,Humidi):
    oled.poweron()
    oled.fill(0)
    #oled.pixel(10, 20, 1)
    graphics.rect(8, 16, 50, 10, 1)
    graphics.rect(70, 16, 50, 10, 1)
    graphics.rect(2, 2, 124, 28, 1)
    graphics.fill_rect(8, 16, Temper/2, 10, 1)
    graphics.fill_rect(70, 16, Humidi/2, 10, 1)
    oled.text(str(Temper)+" C", 18, 6)
    oled.text(str(Humidi)+" %", 80, 6)
    oled.show()



def Oled_bmp(temp, press, alti):
    oled.poweron()
    oled.fill(0)
    #oled.pixel(10, 20, 1)
    graphics.rect(8, 16, 50, 10, 1)
    graphics.rect(70, 16, 50, 10, 1)
    graphics.rect(2, 2, 124, 28, 1)
    graphics.fill_rect(8, 16, temp/2, 10, 1)
    graphics.fill_rect(70, 16, press/40, 10, 1)
    oled.text(str(temp)+" C", 18, 6)
    oled.text(str(press)+" p", 70, 6)
    oled.show()



while True:
    d.measure()

    temp = int(bmp.temperature)

    tempsumme = int((d.temperature() + temp) / 2)

    print("Temperatur: " + str(tempsumme) + "C")
    print("Luftfeuchtigkeit: " + str(d.humidity()) + "%")

    Oled_dht(tempsumme, d.humidity())

    sleep(5)

    press = int(bmp.pressure / 100)
    alti = int(bmp.altitude)

    print(tempsumme, press, alti)

    Oled_bmp(tempsumme, press, alti)

    # logging.logwrite(str(d.temperature()) + "C / " + str(d.humidity()) + "%")

    sleep(5)
