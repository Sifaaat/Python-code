#dictionary

info  ={
     "key ": "value",
     "name": "ApnaCollege",
     "learning" : "coding",
     "age" : 22 ,
     "is_adult" : True
}

print(info)
print(type(info))

info["name"] = "Sifat"
print(info)
#nested Dictionary
student = {
     "name" : "Sifat",
     "subject" : {
         "phy" : 97,
         "chem":98
     }
}
print(student)
print(len(student))