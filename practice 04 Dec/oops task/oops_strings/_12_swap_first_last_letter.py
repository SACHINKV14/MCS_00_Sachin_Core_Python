class Swapfl():
    def __init__(self):
        pass
    def swap_f_l(self,string1):
        start=string1[0]     #start=s
        end=string1[-1]      #end=n
        swapped_string=end+string1[1:-1]+start  #cancsting n+achi+s
        print(swapped_string) #nachins

# should implement removing special characters
user_input = input("Enter string here:")
s1=Swapfl()
s1.swap_f_l(user_input)
