from hub2hub import CityHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a city hub
ble = ble_handler()
Chub = CityHub(ble)

# connect to a city hub: press green button on the city hub
Chub.connect()

k = 0
while True:
    Chub.led(k%11)

    k+=1
    sleep_ms(1000)