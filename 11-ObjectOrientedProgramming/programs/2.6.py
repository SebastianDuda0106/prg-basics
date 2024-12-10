class Phone():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        self.poweron=False
        self.battery=100
        self.flash=False

    def powerbutton(self):
        if self.poweron==False:
            self.poweron=True
        elif self.poweron==True:
            self.poweron=False

    def flashbutton(self):
        if self.flash==False and self.battery>0:
            self.flash=True
            self.battery-=1
        elif self.flash==True:
            self.flash=False
    
    def display_info(self):
        print(f"My phone is a {self.model} {self.brand} ")
        print(f"It was made in {self.year}.")
        if self.battery>0:
            if self.flash:
                print("The phones flashight is turned on")
                self.battery-=1
            else:
                print("The phones flashight is turned off")
            if self.poweron:
                print("The phone is turned on")
                print(f"The battery is at {self.battery}%")
            else:
                print("The phone is turned off")
        else:
            print('The battery is dead')
    

def main():
    myphone=Phone("Samsung","A34",2020)
    myphone.powerbutton()
    myphone.flashbutton()
    myphone.flashbutton()
    myphone.display_info()
    return 0

if __name__=='__main__':
    main()