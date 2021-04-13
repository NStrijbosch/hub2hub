from hub2hub import MoveHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a city hub
ble = ble_handler()
Mhub = MoveHub(ble)

# connect to a city hub: press green button on the city hub
Mhub.connect()

k = 0
while True:
    Mhub.led(k%11)

    k+=1
    sleep_ms(1000)