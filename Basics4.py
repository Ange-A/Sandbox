student_name_1 = 'Itika'  
student_name_2 = 'Parker' 

records = {'Itika': 90, 'Arshia': 92}
def marks(student_name):
  for a_student in records:
    if a_student == student_name:
       return records[a_student]
       break
  else:
    return f'There is no student of name {student_name} in the records'
  
print( f"Marks of {student_name_1} are: ", marks( student_name_1 ) )  
print( f"Marks of {student_name_2} are: ", marks( student_name_2 ) )  

#sum of squares of the first 15 natural numbers

num = 15

#summation initialization and a counter  for iteration

summation = 0
c = 1

while c <= num:
 summation = c**2 + summation
 c = c + 1

print("The sum of squares is", summation)  


num =[34,12,54,23,75,34,11]

def prime_number(number):
  condition = 0
  iteration = 2
  
  while iteration <= number /2:
    if  number % iteration == 0:
        condition = 1
        break
    iteration  = iteration + 1
    
  if condition == 0:
     print(f"{number} is a PRIME number")
  else:
      print(f"{number} is not a PRIME number")
      
for i in num:
  prime_number(i)
      
      
#multiplication of 21

num = 21


list_ = [3, 5, 1, 4, 6]
squares = []

while list_:
  squares.append((list_.pop()) **2)
  
print(squares)



list= [1,2,3,4]
count = 1

for i in list:
  if i == 4:
     print('item matched')
     count = count + 1;
     break
   
print ("found at", count, "location")



for iterator in range(10,21):
  
  if iterator == 15:
     continue
   
  print(iterator)
  
#Skip string letter
string = "AngeAduhire"

iterator = 0

while iterator < len(string):
  
  if string [iterator] == 'A':
     continue
  
  print(string[iterator])
  iterator + =1


counter = 1

print("Multiplication table of: ", num)

while counter <= 10:
    ans = num * counter
    print(num, 'x', counter, '=',ans)
    counter += 1
    
list_ = 
    


name = "Bro Code"

first_name =  name [::2]
reversed_name = name[::-1]
    
    
for i in range(11):
    print(i)

import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year")
    
    
for i in range(50, 100+1, 2):
    print(i)
