class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lst=[]
        for i in range(1,len(min(str1,str2))+1):
            a=int(len(str1)/len(str2[0:i]))
            if str2[0:i] in str1 and str2[0:i]*a==str1:
                lst.append(str2[0:i])
                # print(lst)
        if len(lst)>0:
            print("here")
            print(lst[0])
        else:
            print("")


str1 = "ABCABC"; str2 = "ABC"
# str1="LEET"
# str2="CODE"
# str1 = "ABABAB";str2 = "ABAB"

# str1="TAUXXTAUXXTAUXXTAUXXTAUXX"
# str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
s1=Solution()
s1.gcdOfStrings(str1,str2)