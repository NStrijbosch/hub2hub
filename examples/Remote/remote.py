from hub2PU Remote, ble_handler
from time import sleep_ms

ble = ble_handler()
Remote = Remote(ble)
Remote.connect()

RemoteLed = Remote.led
RemoteLeft = Remote.left
RemoteRight = Remote.right

k = 0
while True:
    RemoteLed(k%11)
    print('Left plus pressed: ', RemoteLeft.plus.is_pressed())
    print('Right plus was pressed: ', RemoteRight.plus.was_pressed())

    k+=1
    sleep_ms(1000)