n = int(input("Enter a number:"))
num =n
while num > 0:
    last_number = num % 10
    print(last_number)
    num = num//10
