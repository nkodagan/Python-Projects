nums = [1,5,2,4,3]
print(min(nums))


print(max(nums))

print(sum(nums))

courses = ['History', 'math', 'Science']

for item in enumerate (courses, start=1):
    print(item)

color = ['yellow', 'blue', 'pink']
color_str = ','.join(color)

print(color_str)

new_list = color_str.split(' - ')
print(new_list)
