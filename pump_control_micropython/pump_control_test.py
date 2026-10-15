from machine import * 
from DIYables_MicroPython_Ultrasonic_Sensor import UltrasonicSensor
import time

pump = Pin(23, Pin.OUT, value = 0)
sensor = UltrasonicSensor(trig.pin = 16, echo.pin = 17)
led = Pin(2, Pin.OUT, value = 0)
button = Pin(33, Pin.IN, Pin.PULL_UP)

def pump_on():
    print("pump in on")
    pump.value(1)
    time.sleep(5)

def esp_config():
    led.value(1);
    print("esp conntected")

def button_detect():
    current_state = button.value();
    if current_state != button.value():
        time.sleep(0.05);
        pump_on()
        time.sleep(1);

def sensor_config():
    sensor = set_detection_threshold(40)
    sensor.enable_filter(num_samples=20)


def sensor_update():
    sensor.loop()
    dist = sensor.get_distance()
    if dist < 5:
        #turn on all 4 diodes
        print("full tank")
    else if dist < 12:
        #trun on 3 diodes
        print("medium water level")
    else:
        #turn on last diode
        print("lacking water")

esp_config()
sensor_config()

while true:
    button_detect()
    sensor_update()

    
            
            
            
    


