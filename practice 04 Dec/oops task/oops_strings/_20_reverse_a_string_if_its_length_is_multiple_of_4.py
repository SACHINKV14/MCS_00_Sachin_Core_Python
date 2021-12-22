class String:
    def rev_str(self,str1):
        lst = [x[::-1] for x in str1 if len(x) % 4 == 0 and x != 0]
        str2 = " ".join(lst)
        print(str2)

str1=['sa','sach','sachnagu','sac','a']
s1=String()
s1.rev_str(str1)


