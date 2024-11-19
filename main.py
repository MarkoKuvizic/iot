import sys
import os
from threading import Thread
from component import Component
from dht.DHT11 import *
import pir.pir as pir
import keyboard.keyboard as keyboard


def getPin(pinString):
    eval(pinString.replace("-pin", ""))


def getPins(pinString):
    retVal = []
    for v in pinString.replace("-pin", "").split("/"):
        retVal.append(eval(v))
    return retVal


def console_driver():
    while True:
        x = input(">")
        if x.upper() == "X":
            os._exit(0)


def main():
    config = sys.argv

    DHT1 = None
    DHT2 = None
    RPIR1 = None
    RPIR2 = None
    DPIR = None
    DMS = None
    if "-pin" in config[-1]:
        DHT1 = Component("DHT1", loop, [getPin(config[-1])])
    elif "-sim" in config[-1]:
        DHT1 = Component("DHT1", sim, [])
    if "-pin" in config[-2]:
        DHT2 = Component("DHT2", loop, [getPin(config[-2])])
    elif "-sim" in config[-2]:
        DHT2 = Component("DHT2", sim, [])
    if "-pin" in config[-3]:
        RPIR1 = Component("RPIR1", pir.loop, [getPin(config[-3])])
    elif "-sim" in config[-3]:
        RPIR1 = Component("RPIR1", pir.sim, [])
    if "-pin" in config[-4]:
        RPIR2 = Component("RPIR2", pir.loop, [getPin(config[-4])])
    elif "-sim" in config[-4]:
        RPIR2 = Component("RPIR2", pir.sim, [])
    if "-pin" in config[-6]:
        DPIR = Component("DPIR", pir.loop, [getPin(config[-6])])
    elif "-sim" in config[-6]:
        DPIR = Component("DPIR", pir.sim, [])
    if "-pin" in config[-5]:
        DMS = Component("DMS", keyboard.loop, [getPins(config[-5])])
    elif "-sim" in config[-5]:
        DMS = Component("DMS", keyboard.sim, [])
    threadDHT1 = Thread(target=DHT1.drive)
    threadDHT2 = Thread(target=DHT2.drive)
    threadRPIR1 = Thread(target=RPIR1.drive)
    threadRPIR2 = Thread(target=RPIR2.drive)
    threadDPIR = Thread(target=DPIR.drive)
    threadDMS = Thread(target=DMS.drive)
    threadMain = Thread(
        target=console_driver,
    )
    threadDHT2.start()
    threadDHT1.start()
    threadRPIR1.start()
    threadRPIR2.start()
    threadDPIR.start()
    threadDMS.start()
    threadMain.start()


if __name__ == "__main__":
    main()
