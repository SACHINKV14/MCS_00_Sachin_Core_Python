class CountWords():
    OUT = 0
    IN = 1
    def countwords(self,mystring):
        state = CountWords.OUT
        wc = 0
        for i in range(len(mystring)):
            if (mystring[i] == ' ' or mystring[i] == '\n' or
                string[i] == '\t' or mystring[i] == ','):
                state = CountWords.OUT
            elif state == CountWords.OUT:
                state = CountWords.IN
                wc += 1
        return wc

me=CountWords()
string = input("enter name:")
print(me.countwords(string))
