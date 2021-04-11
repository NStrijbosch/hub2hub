from hub2hub import ble_handler, Mario
from time import sleep_ms

ble = ble_handler()
mario = Mario(ble)

mario.connect()

while True:
        
    barcode, color = mario.barcode.get()
    print('barcode: ', barcode, 'color: ', color)
    sleep_ms(100)
