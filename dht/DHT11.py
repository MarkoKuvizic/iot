#!/usr/bin/env python3

try:
    import RPi.GPIO as GPIO
except:
    pass
import random as rdm
import time
from . import LA_DHT as DHT


def loop(name, pins):
    DHTPin = pins[0]
    dht = DHT.DHT(DHTPin)  # create a DHT class object
    sumCnt = 0  # number of reading times
    while True:
        sumCnt += 1  # counting number of reading times
        chk = (
            dht.readDHT11()
        )  # read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        print("The sumCnt is : %d, \t chk    : %d" % (sumCnt, chk))
        if (
            chk is dht.DHTLIB_OK
        ):  # read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            print("DHT11,OK!")
        elif chk is dht.DHTLIB_ERROR_CHECKSUM:  # data check has errors
            print("DHTLIB_ERROR_CHECKSUM!!")
        elif chk is dht.DHTLIB_ERROR_TIMEOUT:  # reading DHT times out
            print("DHTLIB_ERROR_TIMEOUT!")
        else:  # other errors
            print("Other error!")

        print(
            "Humidity : %.2f, \t Temperature : %.2f \n"
            % (dht.humidity, dht.temperature)
        )
        time.sleep(2)


def sim(name, pins=[]):
    for h, t in generate_values():
        print(name, " Humidity : %.2f, \t Temperature : %.2f \n" % (h, t))
        time.sleep(2)


def generate_values(initial_temp=25, initial_humidity=20):
    temperature = initial_temp
    humidity = initial_humidity
    while True:
        temperature = temperature + rdm.randint(-2, 2)
        humidity = humidity + rdm.randint(-2, 2)
        if humidity < 0:
            humidity = 0
        if humidity > 100:
            humidity = 100
        yield humidity, temperature


if __name__ == "__main__":
    print("Program is starting ... ")
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
