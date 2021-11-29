
input_score = list(map(int, input("Enter a multiple value: ")
subject=input_score.split()
m,s,so,k,h,e=input_score.split()


print("score in maths: ", m)
print("score in science: ", s)
print("score in social: ", so)
print("score in kannada: ", k)
print("score in hindi: ", h)
print("score in english: ", e)
print()


total = m + s + so + k + h + e
print('total is :',total)