tuple_1 = ('His','math','phy','compsci')


#tuple is immutable. list can be modified. tuple is to look through.

#sets are files that are values without duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}

print('Math' in cs_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))

#Empty Lists
Empty_list = []
empty_list = list()

#Empty Typles
empty_tuples = ()
empty_tuples = tuple()

#empty sets

empty_set = {} # NOTTHIS
empty_set = set()

