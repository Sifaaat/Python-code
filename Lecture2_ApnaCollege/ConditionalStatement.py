age = int(input("Enter your age: "))

#nesting
if (age >= 18):
    if (age>=80) :
        print("Cannot allow to drive")
    else :
        print("Can drive")
else :
    print("Can't drive")


#WAP to check if a number entered by the user is odd or even

number = int(input("Enter a number: "))

if (number%2 ==0):
    print("Even")
else:
    print("Odd")

#WAP to find the greatest of 3 numbers entered by the user

number1 =int(input("Enter a number: "))
number2 =int(input("Enter another number: "))
number3 =int(input("Enter another number: "))

if (number1>= number2 and number1>=number3) :
    print("Greatest number is : ", number1)

elif (number2>=number3 and number2>=number1) :
    print("Greatest number is : ", number2)

else :
    print("Greatest number is : ", number3)



#WAP to check if a number is a multiple of 7 or not

number = int(input("Enter a number: "))
if (number%7 ==0):
    print("The number is a multiple of 7")

else :
    print("The number is not multiple of 7")