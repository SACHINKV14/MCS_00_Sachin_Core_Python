list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list1_odd=[k for k in list1 if k in list1[0::2]]
print(list1_odd)
list1_even=[v for v in list1 if v in list1[1::2]]
print(list1_even)