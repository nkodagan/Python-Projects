student = {'name': 'John','age':25,'courses':['math', 'compsci']}

print(student)

print(student['courses'])

print(student.get('name'))

print(student.get('phone','Not Found'))


student.update({'name':'Jane','age':26,'phone':'555-5555'})

del student ['age']
print(student)

print(student.values())

for key in student.items():
    print(key)
