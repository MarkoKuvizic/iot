try:
    import RPi.GPIO as GPIO
except:
    pass
import time
import random as rdm
import string

# these GPIO pins are connected to the keypad
# change these according to your connections!

# Initialize the GPIO pins


# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column


def readLine(line, characters, pins, name):
    GPIO.output(line, GPIO.HIGH)

    C1 = pins[4]  # 12
    C2 = pins[5]  # 16
    C3 = pins[6]  # 20
    C4 = pins[7]  # 21
    if GPIO.input(C1) == 1:
        print(name + ":" + characters[0])
    if GPIO.input(C2) == 1:
        print(name + ":" + characters[1])
    if GPIO.input(C3) == 1:
        print(name + ":" + characters[2])
    if GPIO.input(C4) == 1:
        print(name + ":" + characters[3])
    GPIO.output(line, GPIO.LOW)


def loop(name, pins=[]):
    R1 = pins[0]  # 25
    R2 = pins[1]  # 8
    R3 = pins[2]  # 7
    R4 = pins[3]  # 1
    C1 = pins[4]  # 12
    C2 = pins[5]  # 16
    C3 = pins[6]  # 20
    C4 = pins[7]  # 21

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)
    GPIO.setup(R3, GPIO.OUT)
    GPIO.setup(R4, GPIO.OUT)

    # Make sure to configure the input pins to use the internal pull-down resistors

    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    try:
        while True:
            readLine(R1, ["1", "2", "3", "A"], pins, name)
            readLine(R2, ["4", "5", "6", "B"], pins, name)
            readLine(R3, ["7", "8", "9", "C"], pins, name)
            readLine(R4, ["*", "0", "#", "D"], pins, name)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nApplication stopped!")


def generate_values():
    while True:
        yield rdm.randint(0, 100)
        time.sleep(2)


def sim(name, pins=[]):
    for res in generate_values():
        if res < 20:
            print(name, randomChar(res))


def randomChar(N):
    return "".join(rdm.choice(string.ascii_uppercase + string.digits) for _ in range(N))
