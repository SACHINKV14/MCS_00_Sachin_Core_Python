a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

# #number of words using for loop
# test_stirng = a
# total = 1
#
# for i in range(len(test_stirng)):
#    if(test_stirng[i] == ' ' or test_stirng[i] == '\n' or test_stirng[i] == '\t' ):
#       total = total + 1
#
# print("Total Number of Words in our input string is: ", total)

# #Using while loop
# test_stirng = a
# total = 1
# i = 0
# while(i < len(test_stirng)):
#    if(test_stirng[i] == ' ' or test_stirng[i] == '\n' or test_stirng[i] == '\t'):
#       total = total + 1
#    i +=1
#
# print("Total Number of Words in our input string is: ", total)

#using function
def Count_words(test_string):
   word_count = 1
   for i in range(len(test_string)):
      if(test_string[i] == ' ' or test_string[i] == '\n' or test_string[i] == '\t'):
         word_count += 1
   return word_count
test_string = a
total = Count_words(test_string)
print("Total Number of Words in our input string is: ", total)