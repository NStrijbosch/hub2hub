from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Ultrasonic sensor connected to port A
USSensor = Thub.port.A.device

k = 0
while True:
    Thub.led(k%11)
    
    Led1 = 9 if k%4 == 0 else 0
    Led2 = 9 if k%4 == 1 else 0
    Led3 = 9 if k%4 == 2 else 0
    Led4 = 9 if k%4 == 3 else 0
    
    USSensor.mode(5,[Led1, Led2, Led3, Led4])

    k+=1
    sleep_ms(1000)