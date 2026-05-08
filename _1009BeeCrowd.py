name = input()
salary = float(input()) 
totalSales =float(input()) 

commission =float(totalSales*0.15)
finalSalary =salary+commission
print(f"TOTAL = R$ {finalSalary:0.2f}")
