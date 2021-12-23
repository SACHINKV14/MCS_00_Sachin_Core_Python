class String:
    def non_repeating_char(self,str1):
        str1=str1.replace(" ","")
        str1=str1.lower()
        dict1={}
        for k in str1:
            dict1[k]=str1.count(k)
        print(dict1)


str1=input("enter the string:")
s1=String()
s1.non_repeating_char(str1)