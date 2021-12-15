# Python program to find sum of elements in list

# creating a list
list1 = [11, 5, 17, 18, 23]

# using sum() function
total = sum(list1)

# printing total value
print(f'Sum of all elements in given list{list1}:{total}')

print("------------------------------------------")

# Python program to find sum of all
# elements in list using recursion

# creating a list
list2 = [21, 10, 12, 5, 33]

# creating sum_list function
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


# Driver code
total2 = sumOfList(list2, len(list2))

print(f'Sum of all elements in given list{list2}: , {total2}')