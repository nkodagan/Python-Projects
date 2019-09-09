#if True:
    #print('Conditional was True')

#if False:
    ## print('Condition was true')
#language = 'Java'

#if language == 'Python':
    #print ('Language is Python')
#elif language =='Java':
   # print('Language is Java')
#else :
   # print('no Match')

# user = 'Admin'
# logged_in = False

# if user == 'Admin' and logged_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a=[1,2,3]
b=[1,2,3]

print(id(a))
print(id(b))
print(a is b)


