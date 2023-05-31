import time

def countdown(d):
   while d:
      mins, secs = divmod(d, 60)
      timer = '{:02d}:{:02d}'. format(mins,secs)
      print(timer, end="/r")
      time.sleep(1)
      d -= 1
   
  print('Fire in the hole!!')
    

d = input("Enter the time in seconds: ")

countdown(int(d))


import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')

t = input("Enter the time in seconds: ")
countdown(int(t))
  
  
