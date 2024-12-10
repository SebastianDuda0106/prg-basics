import thermometer
import random

therm=thermometer.thermometer(random.randint(34,40))
therm.turnon()
therm.status()
therm.turnoff()
