def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

print("----------------------------")


# Python code to reverse a string
# using loop

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str


s = "Sachin"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))