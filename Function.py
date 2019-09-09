# # # # def hello_func():
# # # # print('Hello Function.')

# # # # hello_func()


# # # def hi_func() :
# # #     return 'Hi.'

# # #     print(hi_Func().upper())
# # # # print(len('Test'))

# # def new_fun(greeting):
# #     return'{}Function.'.format(greeting)

# #     print(new_fun('HI'))

# def hello(greeting,name='You'):
#     return'{},{}'.format(greeting,name)

#     print(hello('Hi', name = Lily))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses = ['Math', 'Art']
info = {'name': 'John','age': 22}
    student_info(*courses, **info)
