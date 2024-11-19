class Component(object):
    def __init__(self, name, driver, pins=[]):
        self.name = name
        self.driver = driver
        self.pins = pins

    def drive(self):
        self.driver(self.name, self.pins)
