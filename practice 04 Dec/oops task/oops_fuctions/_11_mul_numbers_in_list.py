class Mullist:
    def multiply_list(self,list1):
    # Multiply elements one by one
        result = 1
        for x in list1:
            result = result * x
        print(f'multiplyList {list1} is:{result}')
       

list1 = [1, 2, 3,4,5,6,7,8,9]
a1=Mullist()
a1.multiply_list(list1)
