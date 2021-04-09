from hub2hub import Remote, ble_handler
from time import sleep_ms

# Initialize ble handler and a remote
ble = ble_handler()
Remote = Remote(ble)

# connect to a remote: press green button on the remote
Remote.connect()

k = 0
while True:
    Remote.led(k%11)
    print('Left plus pressed: ', Remote.left.plus.is_pressed())
    print('Right plus was pressed: ', Remote.right.plus.was_pressed())

    k+=1
    sleep_ms(1000)