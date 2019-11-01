#https://10.10.10.162/api/Z2OGNqw1IseduPspV9dh3kfOIf2uLFo1Qlr9LzW7/lights
# Connect to the bridge with a particular username
from qhue import Bridge
import time
class SmartLight(object):
    def __init__(self):
        self.b = Bridge("10.10.10.162","Z2OGNqw1IseduPspV9dh3kfOIf2uLFo1Qlr9LzW7")
        print(self.b.url)
        lights = self.b.lights   # Creates a new Resource with its own URL
        print(lights.url)    # Should have '/lights' on the end
        # Let's actually call the API and print the results
        print(lights())
    def turn_on(self,number):
        self.b.lights[number].state(on=True)

    def turn_off(self, number):
        self.b.lights[number].state(on=False)

    def control_intensity(self,number,intensity):
        self.b.lights[number].state(bri=intensity)
