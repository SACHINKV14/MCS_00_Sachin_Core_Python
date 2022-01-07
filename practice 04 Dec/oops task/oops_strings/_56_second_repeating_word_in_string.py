class String:
    def second_repeating_word(self,str1):
        lst2=[]
        lst3=[]
        for i in str1.split():
            if i not in lst2:
                lst2.append(i)
            elif i in lst2:
                lst3.append(i)
        if len(lst3)<=1:
            print('no second repeating word in the string')
        else:
            print(f'second repeating word is:{lst3[1]}')



str1=input("enter the string:").lower()
s1=String()
s1.second_repeating_word(str1)