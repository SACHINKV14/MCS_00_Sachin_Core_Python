class String:
    def int_with_star(self,int1,num):
        str2 = '*'
        print(f'integer with append zeros on left side:{str(int1)+(str2 * num) }')


int1=99
num=int(input("enter number of stars:"))
s1=String()
s1.int_with_star(int1,num)