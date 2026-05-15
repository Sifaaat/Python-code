#WAF to print the length of a list(list is the parameter)

cities =["Dhaka","Ctg","Gazipur","cumilla","Faridpur"]

def print_len(list):
    print(len(list))

print_len (cities)


numbs =[1,2,3,4,5]

def num_len(x):
    print(len(x))

num_len(numbs)

#WAF to print the elements of a list in a single line.(list is the parameter)
cities =["Dhaka","Ctg","Gazipur","cumilla","Faridpur"]
def single_line(list):
    for item in list:
         print(item,end=" ")

single_line(cities)


#WAF to find the factorial of n.(n is the parameter)



def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact * i
    print()
    print(fact,end=" ")

factorial(5)

#WAP to convert usdt to bdt

def convertor(usd_val):
    bdt_val =usd_val * 125
    print()
    print(usd_val,"USD =",bdt_val,"BDT")

convertor(5)


#WAF to take input as an integer in function and print ODD if it is odd or print EVEN if even

def number(n):

    if n%2==0:
        print("EVEN")
    else :
        print("ODD")

n=int(input("Enter a number:"))
number(n)