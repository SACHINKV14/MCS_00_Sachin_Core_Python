class String:
    def first_repeating_word(self,str1):
        str2=""
        i2=""
        count1=0
        for i in str1.split():
            # print(i)
            if i not in str2:
                str2+=i
                count1+=1
            elif i in str2:
                print(f'first repeating word is:{i}')
        if count1==len(str1.split()):
            print('no repeating word in the string')


str1=input("enter the string:").lower()
s1=String()
s1.first_repeating_word(str1)