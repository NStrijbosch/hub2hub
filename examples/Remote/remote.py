import hub2PU
from time import sleep_ms

ble = hub2PU.ble_handler()
Remote = hub2PU.Remote(ble)
Remote.connect()

RemoteLeft = Remote.left
RemoteRight = Remote.right

k = 0
while True:
    Remote.led(k%11)
    print('Left plus pressed: ', RemoteLeft.plus.is_pressed())
    print('Left red pressed: ', RemoteLeft.red.was_pressed())
    print('Left min number of presses: ', RemoteLeft.min.presses())
    print('Right plus pressed: ', RemoteRight.plus.is_pressed())
    print('Right red pressed: ', RemoteRight.red.was_pressed())
    print('Right min number of presses: ', RemoteRight.min.presses())

    k+=1
    sleep_ms(1000)