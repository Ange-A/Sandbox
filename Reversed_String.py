#function to reverse a string

def reverse_string(string):
    reversed_str = string[::-1]
    return reversed_str

input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
  
  
