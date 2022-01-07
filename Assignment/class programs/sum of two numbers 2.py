class Sum:
    def __init__(self):

        pass

    def get_numbers(self,p):     #use for loop to reduce the coding
        self.p=p
        for i in range(len(p)):
            D.append(self.p[i])
        print("Numbers are:",D)
    def two_num_sum(self):
        b = set(D)  # to remove duplicate
        # print(b)
        a = list(b)
        for i in a:
            for j in a:
                if (i + j == 7):
                    c = i, j
                    a.remove(j)
                    d.append(c)
                    # print(c)
        print("Two combination numbers for getting  7 is:",d)

p=[1,2,3,4,5,6,7,8,9]
D = []
c = ()
d = []
p1=Sum()
p1.get_numbers(p)
p1.two_num_sum()
