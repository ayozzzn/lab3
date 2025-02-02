# Create a Class.
# To create a class, use the keyword class.
# Create a class named MyClass, with a property named x :
class MyClass:
  x = 5

# Create Object.
# Now we can use the class named MyClass to create objects.
# Create an object named p1, and print the value of x :
p1 = MyClass()
print(p1.x) # 5.

# The __init__() Function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
# Create a class named Person, use the __init__() function to assign values for name and age :
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name) # John.
print(p1.age) # 36.

# The __str__() Function.
# The __str__() function controls what should be returned when the class object is represented as a string.
# The string representation of an object WITHOUT the __str__() function :
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)

# The string representation of an object WITH the __str__() function :
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

# Object Methods.
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Insert a function that prints a greeting, and execute it on the p1 object :
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

# The self Parameter.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# Use the words mysillyobject and abc instead of self :
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties.
# You can modify properties on objects like this :
p1.age = 40

# Delete Object Properties.
# You can delete properties on objects by using the del keyword :
del p1.age

# Delete Objects.
# You can delete objects by using the del keyword :
del p1

# The pass Statement.
class Person:
  pass