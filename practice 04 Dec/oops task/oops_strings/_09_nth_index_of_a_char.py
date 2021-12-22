class String:
    def nth_index(self,str1):
        num=int(input("enter index to see the char:"))
        print(f'char present at entered index in the string :{str1[num]}')

str1='khgljadlkflkbljbljljb;kjn;kfnlb ljbljbhljhb;ibhluh'
s1=String()
s1.nth_index(str1)