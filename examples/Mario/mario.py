from hub2hub import ble_handler, Mario
from time import sleep_ms

ble = ble_handler()
mario = Mario(ble)

mario.connect()

while True:
    gesture = mario.motion.was_gesture(1024)
    barcode, color = mario.barcode.get()
    pants = mario.pants.get()
    print('barcode: ', barcode, 'color: ', color, 'gesture: ', gesture, 'pants: ', pants)
    sleep_ms(100)
