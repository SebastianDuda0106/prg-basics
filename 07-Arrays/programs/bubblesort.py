def bubbleSort(arr):
   arrtemp=0
   n = len(arr)
   for i in range(0,n-1):
      for j in range(0,n-i-2):
         if arr[j] > arr[j+1]:
               arrtemp=arr[j]
               arr[j]=arr[j+1]
               arr[j+1]=arrtemp
   return arr