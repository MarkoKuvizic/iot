try:
	import RPi.GPIO as GPIO
except:
    pass
import random as rdm
import time

def motion_detected(channel):
    print("You moved")
def no_motion(channel):
    print("You stopped moving")

def loop(pins = []):
    PIR_PIN = pins[0]
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motion_detected)
    GPIO.add_event_detect(PIR_PIN, GPIO.FALLING, callback=no_motion)


def generate_values():
    while True:
        yield rdm.randint(0, 100)
        time.sleep(2)
def sim(name, pins = []):
    prev_res = 0
    for res in generate_values():
        if res > 50 and res < 70 and prev_res > 70:
            print(name, " No Motion")
        if res > 70:
            print(name, " Motion")
        prev_res = res