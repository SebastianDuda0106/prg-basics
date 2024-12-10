class TV:
   def __init__(self):
      self.is_on = False
      self.volume=0
      self.channel_no=1
      self.channels=[
         "TV not programmed, no available channels"
      ]

    
   def increase_volume(self):
      if self.volume<10:
         self.volume+=1
   def decrease_volume(self):
      if self.volume>0:
         self.volume-=1


   def turn_off(self):
      self.is_on=False
   
   def turn_on(self):
      self.is_on=True


   def set_channel(self,new_channel_no):
      if self.is_on:
        if new_channel_no in range(len(self.channels)):
            self.channel_no=new_channel_no
        else:
            print(f'Channel "{new_channel_no}" is not in range')

   def set_channels(self,channels_list):
      self.channels=channels_list
      
   def show_channels(self,):
      count=1
      for channel in self.channels:
         print(f'{count}. {channel}')
         count+=1
      print()

      
   def show_status(self):
      if self.is_on:
         print(f'TV is on, channel {self.channel_no} ',end='')
         try:
            print('('+self.channels[self.channel_no-1]+')')
         except:
            print()
         print(f"The Volume is set at {self.volume}/10")
      else:
         print('TV is off')
      print()
      
   def __str__(self):
      if self.is_on:
         retstring=f'TV is on, channel {self.channel_no}'
         try:
            return retstring+' ('+(self.channels[self.channel_no-1])+')'+f"\nThe Volume is set at {self.volume}/10\n"
         except:
            return retstring+f"\nThe Volume is set at {self.volume}/10\n"
      else:
         return'TV is off\n'
      