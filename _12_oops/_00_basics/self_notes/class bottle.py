class bottle:
    def __init__(self,l,m,h):
        self.liters=l
        self.material=m
        self.hot_cold=h
b1=bottle(1,'steel','hot')
print(b1.liters)
print(b1.material)
print(b1.hot_cold)