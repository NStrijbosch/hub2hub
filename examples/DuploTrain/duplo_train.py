from hub2hub import DuploTrain, ble_handler
from time import sleep_ms

# Initialize ble handler and a city hub
ble = ble_handler()
train = DuploTrain(ble)

# connect to a city hub: press green button on the city hub
train.connect()

k = 0
while True:
    train.led(k%11)

    k+=1
    sleep_ms(1000)