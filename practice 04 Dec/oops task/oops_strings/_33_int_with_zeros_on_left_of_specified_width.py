class String:
    def int_with_zero(self,int1,num):
        str2 = '0'
        print(f'integer with append zeros on left side:{str2 * num + str(int1)}')


int1=99
num=int(input("enter number of zeros:"))
s1=String()
s1.int_with_zero(int1,num)