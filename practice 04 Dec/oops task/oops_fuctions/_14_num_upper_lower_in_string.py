class Numb1:
    def countUpperAndLowerCase(self,sentence):
        upper = 0
        lower = 0
        for i in sentence:
            if (i>='A'and i<='Z'):
                upper += 1
            elif (i>='a'and i<='z'):
                lower += 1
        print("Upper case: " + str(upper))
        print("Lower case: " + str(lower))

a1=Numb1()

a1.countUpperAndLowerCase("Hello Sachin")