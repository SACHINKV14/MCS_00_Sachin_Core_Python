#Convert an array to an array of machine values and return the bytes representation
import array as arr
number = arr.array("b", [75,65,82])
c=number.tobytes()
print(c)