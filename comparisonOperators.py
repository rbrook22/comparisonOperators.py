#Using comparison operators to return boolean values

name='Rick'
age=30

print("Does %s equal Rick"%name)
print(name == 'Rick')

print("Does %s not equal Becky"%name)
print(name != 'Becky')

print("Does %s not equal Rick"%name)
print(name != 'Rick')

print('Is %s greater than 25'%age)
print(age > 25)

print("Is 25 less than %s"%age)
print(25<age)


#Using Logical Operators to chain comparison operators 

print('Does %s equal Rick and does %s equal 30' %(name, age))
print(name == 'Rick' and age == 30)

print('Does %s equal Rick or does %s equal 25' %(name, age))
print(name == 'Rick' or age == 25)

print('Does %s equal rick or does %s equal 25' %(name, age))
print(name == 'rick' or age == 25)

print('Does not %s equal Rick and does %s equal 30' %(name, age))
print(not name == 'Rick' and age == 30)