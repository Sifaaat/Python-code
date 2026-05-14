#..................print numbers 1 to 100
i =1
while i<101:
    print(i)
    i=i+1

#..................print numbers 100 to 1
i = 100
while i>0:
    print(i)
    i=i-1
print("Goodbye")

#................#print the multiplication table of a number n

n =int(input("Enter a number"))
i =1
while i<=10:
    print(i*n)
    i=i+1

#.....................print the elements of the following list using loop:

numb =[1,4,9,16,25,36,49,64,81,100]

index = 0
while index < len(numb):
    print(numb[index])
    index +=1


#Search for a number x in this tuple using loop:
numb = [1,4,9,16,25,36,49,64,81,100]

n =int(input("Enter a number"))

i =0
while i < len(numb):
      if(numb[i] == n):
          print("Found at index: ",i)
      i=i+1
