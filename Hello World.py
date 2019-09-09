message = 'Hello World!'
print(message)
message1 = 'Niya\'s coding world'
print(message1)
message2 = "Just trying randomest things with Python's Tecxt editor"
print(message2)

#print welcome message
print('Hello World!')

message = """scooby dooby do was good
cartoon
in the 1990's"""
print(message)
message = 'hello world'
print(len(message))

print(message[0:5])
print(message[6:])
print(message.lower())
print(message.count('Hello World'))
print(message.find)
print(message.find('Universe'))
new_message = message.replace('world','Universe')
print(new_message)
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name+' . Welcome!'
print(message)

message = '{},{}. Welcome!'.format(greeting, name)
print(message)

message =f' {greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))

print(help(str))
