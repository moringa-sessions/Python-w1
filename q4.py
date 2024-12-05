num1 = (input('Enter number one : '))
if num1.isdigit():
    num1 = int(num1)
else:
    while  not  num1.isdigit():
         num1 = (input('Enter number one : '))
       

num2 = input('Enter number two : ')
if num2.isdigit():
    num2 = int(num2)
else:
    while  not  num2.isdigit():
         num2 = (input('Enter number Two : '))

num3 = input('Enter number three : ')
num4 = input('Enter number four : ')
num5 = input('Enter number five : ')

numbers=[int(num1), int(num2), int(num3), int(num4), int(num5)]
def max_number():

        
    maximum=max(numbers)
    return maximum 

print(f"your maximum number is {max_number()}")

