from hub2hub import CityHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a remote
ble = ble_handler()
Chub = CityHub(ble)

# connect to a city hub: press green button on the hub
Chub.connect()

k = 0
while True:
    Remote.led(k%11)

    k+=1
    sleep_ms(1000)