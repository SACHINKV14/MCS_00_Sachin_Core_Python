def test_range(num,r_start,r_end):
    if num in range(r_start,r_end):
        print( f"num:{num} is in range{r_start},{r_end}")
    else :
        print("The number is outside the given range.")

num=int(input("Enter Number:"))
r_start=int(input("Enter range start:"))
r_end=int(input("Enter range end:"))
test_range(num,r_start,r_end)
