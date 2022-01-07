list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list1_odd=[k for k in list1 if k in list1[0::2]]

print(list1_odd)
list1_even=[v for v in list1 if v in list1[1::2]]
print(list1_even)

print("----------------------------------------------------")
str1='A quick brown fox jumps over the lazy dog'
lst_odd=[a for a in str1 if a in str1[0::2]]
lst_even=[b for b in str1 if b in str1[1::2]]

str1_even=""
str1_odd=""

for ele1 in lst_odd:
        str1_odd += ele1
print(str1_odd)

for ele2 in lst_even:
        str1_even += ele2
print(str1_even)