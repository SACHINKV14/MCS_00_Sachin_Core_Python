# set dimensions
x = 2
y = 2
z = 2
#create 3D list
a_3d_list = []

#add `x` empty lists to the 3D list
for i in range(x):
    a_3d_list.append([])

#add `y` empty lists to each of the `x` lists
    for j in range(y):
        a_3d_list[i].append([])

#add initial value of `0` to the innermost list
        for k in range(z):
            a_3d_list[i][j].append(0)

print("--------------------------------------")
# set dimensions
x = 2
y = 2
z = 2
# comprehension to fill a 3D list with `0`s according to the set dimensions
a_3d_list = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]

# OUTPUT
print(a_3d_list)




