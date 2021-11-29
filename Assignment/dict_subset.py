n = int(input("enter number of subjects:"))
sub_marks = {}


def my_marks( n, sub_marks ):
    for i in range(n):
        subjects = input("Enter the subject name:")
        marks = int(input("Enter the marks of the subject:"))
        sub_marks[subjects] = marks
        less_marks_subject = {key: value for key, value in sub_marks.items() if value > 75}
        total_sub_marks = sum(sub_marks.values())
        percentage_of_total_sub_marks = (total_sub_marks / (n * 100)) * 100
        total_less_marks = sum(less_marks_subject.values())
    print(total_sub_marks)
    print(sub_marks)
    print("---------")
    print(less_marks_subject)


my_marks(n, sub_marks)
