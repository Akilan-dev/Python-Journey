from os import name
student = {'name':'John','age':'22','courses': ['Math','Compsci']}

print(student)


print(student['name'])

print(student['courses'])

# get method

print(student.get('name'))

student['phone'] = '36472 36762'
 
print(student.get('phone','Not Found')) # you can add a default value to the key that does not exist

#Update - method


student.update({'name':'Jane','age':25,'phone':'38463 38693'})



##Deleting a specific key value

del student['age']



print(student)


#looping through the dictionary

print(len(student))

print(student.keys())
print(student.values())

print(student.items())


for key, value in student.items():
    print(key,value)