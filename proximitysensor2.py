from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23)
object = False;

#check 5 times in 5 seconds, set object variable accordingly
for x in range(5):
    dist = sensor.distance * 100;
    if dist >= 10:
        object = False;
    if dist < 10:
        object = True;
    sleep(1)
