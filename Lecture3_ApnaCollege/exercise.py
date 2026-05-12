
#WAP to ask the user to enter names of their 3 favourite movies and store them in a list

Movies =[]

favMOvie1=input("Enter a movie: ")
favMOvie2=input("Enter another movie: ")
favMOvie3=input("Enter another movie: ")

Movies.append(favMOvie1)
Movies.append(favMOvie2)
Movies.append(favMOvie3)

print(Movies)


#WAP to check if a list contains a palindrome of elements.
list1 =[1,2,1]
list2 =[1,2,3]

copy_list1 =list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
      print("Palindrome")
else :
      print("Not Palindrome")

copy_list2 =list2.copy()
copy_list2.reverse()
if (copy_list2==list2):
      print("Palindrome")
else :
      print("Not Palindrome")



#WAP to count the number of student with the "A" grade in the following tupe
grade =["C","D","A","A", "B", "B", "A" ]

print(grade.count("A"))