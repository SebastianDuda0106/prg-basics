import tv

def main():
   # object creation
   telewizor=tv.TV()

   # object usage
   print(telewizor)
   telewizor.turn_on()
   print(telewizor)
   telewizor.show_channels()
   telewizor.set_channels(["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"])
   telewizor.show_channels()
   telewizor.set_channel(5)
   telewizor.set_channel(7)
   telewizor.increase_volume()
   telewizor.increase_volume()
   telewizor.increase_volume()
   print(telewizor)
   telewizor.decrease_volume()
   print(telewizor)
   telewizor.turn_off()
   telewizor.show_status()

if __name__ == "__main__":
   main() 