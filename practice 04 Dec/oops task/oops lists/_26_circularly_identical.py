
class Lists:
    def cir_identical(self,list1,list2):
        a1=sorted(list1,reverse=True)
        b1=sorted(list2,reverse=True)
        print(a1),print(b1)
        if a1==b1:
            print("two lists are circularly identical")
        else:
            print("two lists are not circularly identical")


list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
# list2 = [1, 10, 10, 0, 0]
l1=Lists()
l1.cir_identical(list1,list2)