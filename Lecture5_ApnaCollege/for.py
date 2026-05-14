list =[1,2,3,4,5]

for val in list:
    print(val)

#print the elements of the following list using a loop:

numbs =[1,4,9,16,25,36,49,64,81,100]

for val in numbs:
    print(val)


#Search for a number x in this tuple using loop:
numb =(1,4,9,16,25,36,49,64,81,100,49)
x = 49

index =0
for val in numb:
    if (val == x):
        print("Number found at index: ",index)
    index=index+1
