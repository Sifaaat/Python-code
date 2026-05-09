# Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

def Calculation(num1,num2):
    product = num1*num2
    if product <= 1000 :
        return product
    else :
        return(num1+num2)
       
       
n = int(Calculation(20,30))    
print(n)
