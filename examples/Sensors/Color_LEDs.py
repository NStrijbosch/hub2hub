from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Color sensor connected to port A
ColorSensor = Thub.port.A.device

k = 0
while True:
    Thub.led(k%11)
    
    Led1 = 9 if k%3 == 0 else 0
    Led2 = 9 if k%3 == 1 else 0
    Led3 = 9 if k%3 == 2 else 0
    
    ColorSensor.mode(3,[Led1, Led2, Led3])

    k+=1
    sleep_ms(1000)