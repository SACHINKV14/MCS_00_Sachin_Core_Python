print("----single string-------")
a='green'
# print(a[0].capitalize())
# print(a[1:-1])
# print(a[-1].capitalize())
a1=a[0].capitalize()+a[1:-1]+a[-1].capitalize()
print(a1)
print("----single string-------")

print('------in list--------')
colors=['green','blue','yellow']
for word in colors:
    a1 = word[0].capitalize() + word[1:-1] + word[-1].capitalize()
    print(a1)
print('--------------------------------------------------------------')

txt1=input("Enter text here:")
for word in txt1.split():
    a1 = word[0].capitalize() + word[1:-1] + word[-1].capitalize()
    print(a1,end=" ")

# print("------------------------------------------")