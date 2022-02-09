from database import get_even_stu


def get_even_stu(stu):
    if stu % 2 == 0:
        return get_even_stu()
    else:
        return "Fail"

