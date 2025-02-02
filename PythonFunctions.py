# Creating a Function.
# In Python a function is defined using the def keyword :
def my_function():
    print("Hello from a function")

# Calling a Function.
# To call a function, use the function name followed by parenthesis :
def my_function():
    print("Hello from a function")
my_function() 

# Arguments.
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number of Arguments.
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

# Arbitrary Arguments, *args.
# If the number of arguments is unknown, add a * before the parameter name :
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# Keyword Arguments.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs.
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value.
# If we call the function without argument, it uses the default value :
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument.
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values.
# To let a function return a value, use the return statement :
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement.
def myfunction():
  pass

# Positional-Only Arguments.
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments :
def my_function(x, /):
  print(x)
my_function(3)

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments :
def my_function(x):
  print(x)
my_function(x = 3)

# But when adding the , / you will get an error if you try to send a keyword argument.

# Keyword-Only Arguments.
# To specify that a function can have only keyword arguments, add *, before the arguments :
def my_function(*, x):
  print(x)
my_function(x = 3)

# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments :
def my_function(x):
  print(x)
my_function(3)

# But with the *, you will get an error if you try to send a positional argument.

# Combine Positional-Only and Keyword-Only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

# Recursion.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results:")
tri_recursion(6)