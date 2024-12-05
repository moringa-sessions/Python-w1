num1=int(input('Enter number 1 :'))
num2=int(input('Enter number 2 :'))
for num in range(num1,num2):
    if num % 7 == 0:
        continue
    print(num)