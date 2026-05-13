#store following word meanings in a python dictionary:

components ={
    "table":["a piece of furniture","list of facts & figures"],
    "cat": "a small animal"
}
print(components)


#you are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classroom are needed by all students.

subject = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(subject)
print("Classroom needed: ",len(subject))


#WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and add one by one ,Use subject name as key and marks as value.

dictionary1 = {}

paper1 =int(input("enter your 1st paper number"))
paper2 =int(input("enter your 2nd paper number"))
paper3 =int(input("enter your 3rd paper number"))


dictionary1["physics"] = paper1
dictionary1["chemistry"] = paper2
dictionary1["Biology"]=paper3

print(dictionary1)