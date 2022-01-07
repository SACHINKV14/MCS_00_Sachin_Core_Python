# to create a file and read it.
file = open('file1.txt','w')
file.write('A quick brown fox jumps over the lazy dogs')
file.close()


file = open('file1.txt','r')
print(file.read())                  # reading the file upto 20 characters
file.close()

file = open('file1.txt','a')      #open the file
file.write('\n above text contains all the letters in alphabets')
file.close()                     #close the file

with open('file1.txt') as f:            #if we open file with this method no need of closing the file
    data = f.readlines()
    for line in data:
      word = line.split()                              #splitt the lines
      print(word)