# micropython-consentiumthings

Passing tests on ESP 8266 and ESP 32

Developed by Debjyoti Chowdhury from ConsentiumInc


## Installing dependencies and main library

First connect to WiFi with SSID and Psk

```python
import network

ssid = ""
psk = ""

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid,psk)
station.isconnected()
print(station.ifconfig())

```
Then install dependencies and main module using upip
``` python
>>> import upip
>>> upip.install('micropython-urequests')
>>> upip.install('micropython-consentiumthings', '/lib/')

```

## Examples of How To Use 

Making requests to Consentium IoT server

```python
from ConsentiumThings import ThingsUpdate
import utime

api_key = ""

ssid = ""
psk = ""

board = ThingsUpdate(key=api_key)

board.initWiFi(ssid,psk)

while True:
    sensor_val = [1, 2, 3, 4, 5, 6, 7]
    info_buff = ["a", "b", "c", "d", "e", "f", "g"]
    r = board.sendREST(sensor_val=sensor_val, info_buff=info_buff)
    print(r.text)
    utime.sleep(5)
```
