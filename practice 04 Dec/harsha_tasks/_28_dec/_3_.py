# Write a Python program to append text to a file and display the text.
f = open("doc.txt","a")
f.write("this is processing of the selection\n")
f.write("one line\n")
f.write("two line\n")
f.write("third line\n")
f.write("fourth line\n")
f1 = open("doc.txt","r")
result = f1.read()
print(result)
f.close()