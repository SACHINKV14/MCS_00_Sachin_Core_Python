# Python3 code to demonstrate
# Split on last occurrence of delimiter
# using rsplit()
class List1:
    def split_string(self,str1):
        # printing original string
        print("The original string : " + str(test_string))
        res = test_string.rsplit(', ', 1)
        print("The splitted list at the last comma : " + str(res))


# initializing string
test_string = "india, is, good, better, and best"

l1=List1()
l1.split_string(test_string)