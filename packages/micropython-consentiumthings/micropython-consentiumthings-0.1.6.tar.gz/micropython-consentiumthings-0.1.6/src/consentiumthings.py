import network
import urequests as requests
import ujson as json


class ThingsUpdate:
    payload = {}
    station = network.WLAN(network.STA_IF)
    station.active(True)

    def __init__(self, key):
        self.key = key

    def initWiFi(self, ssid, psw):
        self.station.connect(ssid, psw)
        print("Got IP:",self.station.ifconfig()[0])


    def sendREST(self, info_buff, sensor_val):
        url = "http://consentiuminc.online/update?send_key="+self.key
        sensor_num = len(sensor_val)
        if self.station.isconnected():
            if sensor_num == 1:
                url = url+"&sensor1="+str(sensor_val[0])+"&info1="+str(info_buff[0])
            if sensor_num == 2:
                url = url+"&sensor1="+str(sensor_val[0])+"&info1="+str(info_buff[0])+"&sensor2="+str(sensor_val[1])+"&info2="+str(info_buff[1])
            if sensor_num == 3:
                url = url+"&sensor1="+str(sensor_val[0])+"&info1="+str(info_buff[0])+"&sensor2="+str(sensor_val[1])+"&info2="+str(info_buff[1])+"&sensor3="+str(sensor_val[2])+"&info3="+str(info_buff[2])
            if sensor_num == 4:
                url = url+"&sensor1="+str(sensor_val[0])+"&info1="+str(info_buff[0])+"&sensor2="+str(sensor_val[1])+"&info2="+str(info_buff[1])+"&sensor3="+str(sensor_val[2])+"&info3="+str(info_buff[2])+"&sensor4="+str(sensor_val[3])+"&info4="+str(info_buff[3])
            if sensor_num == 5:
                url = url+"&sensor1="+str(sensor_val[0])+"&info1="+str(info_buff[0])+"&sensor2="+str(sensor_val[1])+"&info2="+str(info_buff[1])+"&sensor3="+str(sensor_val[2])+"&info3="+str(info_buff[2])+"&sensor4="+str(sensor_val[3])+"&info4="+str(info_buff[3])+"&sensor5="+str(sensor_val[4])+"&info5="+str(info_buff[4])
            if sensor_num == 6:
                url = url+"&sensor1="+str(sensor_val[0])+"&info1="+str(info_buff[0])+"&sensor2="+str(sensor_val[1])+"&info2="+str(info_buff[1])+"&sensor3="+str(sensor_val[2])+"&info3="+str(info_buff[2])+"&sensor4="+str(sensor_val[3])+"&info4="+str(info_buff[3])+"&sensor5="+str(sensor_val[4])+"&info5="+str(info_buff[4])+"&sensor6="+str(sensor_val[5])+"&info6="+str(info_buff[5])
            if sensor_num == 7:
                url = url+"&sensor1="+str(sensor_val[0])+"&info1="+str(info_buff[0])+"&sensor2="+str(sensor_val[1])+"&info2="+str(info_buff[1])+"&sensor3="+str(sensor_val[2])+"&info3="+str(info_buff[2])+"&sensor4="+str(sensor_val[3])+"&info4="+str(info_buff[3])+"&sensor5="+str(sensor_val[4])+"&info5="+str(info_buff[4])+"&sensor6="+str(sensor_val[5])+"&info6="+str(info_buff[5])+"&sensor7="+str(sensor_val[6])+"&info7="+str(info_buff[6])

        res = requests.get(url=url)
        return res.json()