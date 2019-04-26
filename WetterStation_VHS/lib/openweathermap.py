import urequests
import json

class Weather:

    def __init__(self, api, ort):
        self.api = api
        self.ort = ort

    def fivedays(self):
        response = urequests.get("http://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}".format(self.ort, self.api))
        #print(response.content)
        jdata = response.json()
        #print(jdata)
        count = jdata['list'][0]
        print(count)
        for i in range(len(jdata['list'])):
            stadt = jdata['city']['name']
            wind = jdata['list'][i]['wind']
            wetter = jdata['list'][i]['weather'][0]['description']
            #temp = round(jdata['list'][i]['main']['temp'] - 273.15, 2)
            test = round(jdata['list'][i]['main']['temp_max'] - 273.15, 2)
            day = jdata['list'][i]['dt_txt']
            print(stadt + ': ' + day)
            print('Wind: ' + str(round(wind['speed'], 0)) + ' aus: ' + str(wind['deg']))
            print(wetter)
            #print(temp)
            print(str(test) + '\n')

    def thisday(self):
        response = urequests.get("http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(self.ort, self.api))
        #print(response.content)
        jdata = response.json()
        #print(jdata)
        wind = jdata['wind']
        wetter = jdata['weather'][0]['description']
        icon = jdata['weather'][0]['icon']
        temp = round(jdata['main']['temp'] - 273.15, 2)
        data = [str(round(wind['speed'], 0)), str(wind['deg']), wetter, temp, icon]
        return data

class weatherStation:
    def __init__(self, api, ort):
        self.api = api
        self.ort = ort

    pass
