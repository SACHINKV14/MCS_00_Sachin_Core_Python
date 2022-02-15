class Student:
    def _init_(self):
        self.roll = 0
        self.sub_marks ={}
#entery of sub name and marks
    def enter_values(self,n):
        for i in range(0,n):
            self.sub = input("Enter subject : ")
            self.marks = int(input("Enter marks : "))
            self.sub_marks[self.sub] = self.marks
    #fail subject re_enter marks
    def enter_again(self):
        for key,value in self.sub_marks.items():
            if(value < 75):
                print("Enter marks of subject ",key," : ")
                self.sub_temp = int(input())
                self.sub_marks[key] = self.sub_temp


    def grade(self,sub_marks,n):
        self.sum = 0
        for i in self.sub_marks.values():
            self.sum += i
        self.avgall = self.sum*100/(n*100)
        if(self.avgall > 90):
            print("Average all = ",self.avgall)
            print("Distinction")
            self.markslist = self.list(self.sub_marks.values())
            print("marklist = ",self.markslist)
            top1 = max(self.markslist)
            print("Top1 = ",self.top1)
            self.markslist.remove(top1)
            top2 = max(self.markslist)
            print("Top2 = ", self.top2)
            self.markslist.remove(top2)
            top3 = max(self.markslist)
            print("Top3 = ",self. top3)
            self.markslist.remove(top3)
            if(((self.top1 + self.top2 + self.top3)*100/300) > 95):
                print("Gold medal")
        elif(75 < self.avgall < 90):
            print("Average")
        elif(self.avgall < 75):
            print("Fail")

        n = int(input("Enter the number of subjects : "))
        sub_marks = {}
        enter_values(n,sub_marks)    #here

    def result(self,n):
        self.count_fail = 0
        if(3 <= n <= 7):
            for i in self.sub_marks.values():
                if(i < 75):
                    self.count_fail += 1
                    print("Count fail = ",self.count_fail)
            if(self.count_fail==0):
                grade(self.sub_marks,n)  #here
            elif(self.count_fail <= 3):
                print("Chance again")
                enter_again(n,self.sub_marks)   #here
                grade(self.sub_marks, n)     #here
            else:
                print("FAIL!!!")
        elif(n > 7):
            self.count_fail = 0
            self.failed = []
            for i in list(self.sub_marks.values()):
                if(i < 75):
                    self.count_fail += 1
                    failed.append(i)     #here
            if(self.count_fail >= 5):
                print("FAIL IN MORE THAN 4!!!")
                print("DEBARRED !!!")
            else:
                self.sum = 0
                for j in self.failed:
                    self.um += j
                self.avg = self.sum*100/((len(self.failed))*100)
                if(65 <= self.avg <= 75):
                    print("Chance again !!!")
                    enter_again(n,self.sub_marks)
                elif(self.avg < 65):
                    print("FAILED !!!")

    def student_show(self):
        self.grade(self.sub_marks,'n')
        self.result()
        print(self._roll, "\t\t", self.name, "\t\t", self.total, "\t\t", self.grade, "\t\t",self._result)


# Student object
s = Student()
#s.enter_values()
s.enter_again()
s.student_show()