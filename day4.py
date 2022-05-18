name= "hi! there timmy"
print(name[3:8])
print(name[3:8:2])

string ="121" # *12345"
bool = (string == string[::-1])
print(bool)

str  = "Hi!I am there"
print(len(str))
#remove white space(left)
str  = " Hi!I am there"
print(str.strip())
str  = "Hi!I am there"
print(str.strip("Hi"))

#spliting into list
str  = "Hi!I am there"
print(str.split("Hi"))
#replace by other words
str  = "Hi!I am there"
print(str.replace("Hi","Hlw"))
print(str.replace("there","Here"))
#For Upper Case
str  = "Hi!I am there"
print(str.upper())
#For First letters upper case
str  = "Hi! I am there"
print(str.capitalize)
#sentence startswith ,endswith
str  = "Hi! I am there"
print(str.startswith("Hi!"))
print(str.startswith("n"))
print(str.endswith("e"))
#index position of where it was found
str  = "Hi! I am there"
print(str.index("e")) #count the first e
#count,Can count the specific character
str  = "Hi! I am there"
print(str.count("e"))
#find the index of character


#bool
print(bool(None))




#take user input and output you current age
a = int(input("What year did you born?"))
age = (2021-a)
print(f"Your age is {age}")




#print(bool()) #by default false
#print(bool(0))
#print(bool(1))
#print(bool(""))
#print(bool("A"))
#print(bool({()}))
#print(bool({}))
#print(bool(set()))
#print(range(6))
