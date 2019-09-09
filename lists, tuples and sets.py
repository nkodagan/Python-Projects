
courses = ['history', 'maths', 'physics', 'compsci']
#to create a list use [] and separate them by comma
print(courses)
print(courses[0])
print(len(courses))
print(courses[3])
print(courses[-1])

print(courses[:2])

print(courses[2:])



courses.append('Art')
print(courses)


courses.insert(0,'Art')
print(courses)

courses_2 = ['Art', 'Education']

courses.insert(0, courses_2)
print(courses)

courses.extend(courses_2)
print(courses)

courses.remove('math')

courses.pop()
print(courses)

popped = (courses.pop)
print(popped)
print(courses)

courses.sort()
print(courses)

#descending order

courses.sort(reverse = True)
print(courses)

nums = [1,5,6,7,9]
courses.sort(reverse = True)
print(courses)
sorted_nums = sorted(nums)







