


class Solution:
    def findWords(self, words):
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        list1=[]
        for i in keyboard:
            for j in words:
                for k in j.lower():
                    if k not in i:
                        break
                else:
                    list1.append(j)
        print(list1)






# words = ["Hello", "Alaska", "Dad", "Peace"]
words = ["omk"]
s1=Solution()
s1.findWords(words)
