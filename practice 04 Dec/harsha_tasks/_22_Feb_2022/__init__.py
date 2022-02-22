n = int(input())
lstA = []
lstB = []
for i1 in range(n):
    inp = input()
    inp1=inp.split(" ")
    B = int(inp1[-1])
    A =inp.replace(inp[-1],"")

print("A",A)
print("B",B)