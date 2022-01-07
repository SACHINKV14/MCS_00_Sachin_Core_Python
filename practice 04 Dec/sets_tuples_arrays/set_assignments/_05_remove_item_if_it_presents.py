s5 = {1, 4, 5, 7, 2, 6, 3}
print("Before remove ----", s5)
num5=int(input('enter item to remove:'))

if num5 in s5:
    s5.discard(num5)
    print("item is present and removed from set:", s5)
else:
    print("item is not present in set")