class thermometer:
    def __init__(self,temperature):
        self.temperature=temperature
        self.ison=False

    def turnon(self):
        self.ison=True
    def turnoff(self):
        self.ison=False

    def status(self):
        if self.temperature in range(34,43):
            print('Temperature: ',self.temperature,end='')
            if self.temperature  in range(37,41):
                print(" (fever)")
            if self.temperature  in range(41,43):
                print(" (CRTICAL TEMPERATURE!!)")
                