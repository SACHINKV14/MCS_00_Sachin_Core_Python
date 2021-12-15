class Numb1:
    def test_range(self,num,r_start,r_end):
        if num in range(r_start,r_end):
            print( f"num:{num} is in range{r_start},{r_end}")
        else :
            print("The number is outside the given range.")


r_start=int(input("Enter range start:"))
r_end=int(input("Enter range end:"))
num=int(input("Enter Number to check its in range:"))
a1=Numb1()
a1.test_range(num,r_start,r_end)
