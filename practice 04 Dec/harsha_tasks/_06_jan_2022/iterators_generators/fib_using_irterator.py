# 2. Using __iter__ to Make Iterators from Your Objects
class FibIterable:
    """
    this class is a generates a well known sequence of numbers
    """

    def __init__(self, iLast=1, iSecondLast=0, iMax=500):
        self.iLast = iLast
        self.iSecondLast = iSecondLast
        self.iMax = iMax  # cutoff

    def __iter__(self):
        return self  # because the object is both the iterable and the iterator

    # __next__
    # second last = 0
    # last = 1
    # second last = 1
    # last = 1
    # 0 1 1 2 3 5 3+5
    def __next__(self):
        iNext = self.iLast + self.iSecondLast
        if iNext > self.iMax:
            raise StopIteration()
        self.iSecondLast = self.iLast
        self.iLast = iNext
        return iNext


print("----------My own customized Iterator through AUTO------------")
myObj = FibIterable()  # list1 = [1,2,3]
# print(myObj)
print("----Fib Series-----")
for value in myObj:
    print(value)
