class Pangram:
    def str_all_alphabets(self,str1,lst3):
        # str15 = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
        # str15 = str15.split(",")
        # print("above or below")
        str15 = 'abcdefghijklmnopqrstuvwxyz'
        count_alpha=0
        missing_char=[]
        for a in str15:
            if a not in lst3:
                missing_char.append(a)
                count_alpha += 1
        print(f'number of alphabets missing in string is:{count_alpha}')
        print(f'chars which are missing in string is :{missing_char}')
        if count_alpha == 0:
            # print(f'Entered string \"{str1}\" is pangram')
            print(f'Entered string  is pangram')
        else:
            # print(f'Entered string \"{str1}\" is not pangram')
            print(f'\"Entered string  is not pangram\"')


str1=input("enter only alpha character string:").lower()
lst3=[]
lst2=list(str1)
lst12=lst2.copy()
for letter in lst12:
    if letter.isalpha():
        lst3.append(letter)
s1=Pangram()
s1.str_all_alphabets(str1,lst3)





print("--------------------------------------------------------------")

class Demo:
    def _init_(self):
        pass
    def chck(self,str1):
        a=list(range(97,97+26))
        b=[]
        boo=False
        for i in a:
            b.append(chr(i))

        for i in b:
            if i not in str1:
                boo=False
                break
            else:
                boo=True

        return boo



d=Demo()
b=input("enter the text")
c=d.chck(b)
if  c==False:
    print("not validd")
else:
    print("valid")

