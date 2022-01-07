class total:
    def __init__(self):
        self.mark1=0
        self.mark2=0
        self.mark3=0
        self.mark4=0
        self.mark5=0
        self.mark6=0
        self.total=0
        self.percentage=0
        self.num_of_subjects=6
    def get_marks(self):
        self.mark1 = int(input("Enter student mark : "))
        self.mark2 = int(input("Enter student mark : "))
        self.mark3 = int(input("Enter student mark : "))
        self.mark4 = int(input("Enter student mark : "))
        self.mark5 = int(input("Enter student mark : "))
        self.mark6 = int(input("Enter student mark : "))
        self.total=self.mark1+self.mark2+self.mark3+self.mark4+self.mark5+self.mark6
        self.percentage=(self.total / (self.num_of_subjects * 100)) * 100
    def print_total_marks(self):
        print("total marks is:",self.total)
        print("percentage of marks is:",self.percentage)
    def result(self):
        if self.percentage==100:
            print("Student awarded gold medal")
        elif self.percentage>90:
            print("Distinction")
        elif self.percentage > 75 and self.percentage < 90:
            print("Student got first class")
        else:
            print("student is failed")

a=total()
a.get_marks()
a.print_total_marks()
a.result()