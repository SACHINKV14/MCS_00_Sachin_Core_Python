class Uid:
    def print_uid(self,a):
        print(id(a))

a=10
a1 = Uid()
a1.print_uid(a)
