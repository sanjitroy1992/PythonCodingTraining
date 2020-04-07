def Grading_Students():
    n = int(input())
    # marks_list = []
    for _ in range(n):
        mark = int(input())
        if mark <38:
            new_mark = mark
        elif ((mark//5)*5+5- mark == 3):
            new_mark = mark
        elif ((mark//5)*5+5- mark< 3):
            new_mark = (mark//5)*5+5
        # marks_list.append(new_mark)
        print(new_mark)


Grading_Students()