# #---------------------------------------------------- <1> ----------------------------------------------------#
# class Object:
#     def __init__(listdata, lst1, lst2, num):
#         listdata._lst1 = lst1
#         listdata._lst2 = lst2
#         listdata._num = num
# class MyList(Object):
#     def returnit(listmutation): 
#         print(
#             "Merge operation: {}".format(listmutation._lst1 + listmutation._lst2),
#             "\nDivision operation: {}, {}".format(listmutation._lst1 * listmutation._num, listmutation._lst2 * listmutation._num)
#         )
#     def intostr(stringitlist):
#         str1 = "-"
#         str1 = str1.join(stringitlist._lst1)
#         str2 = "-"
#         str2 = str2.join(stringitlist._lst2)
#         print(
#             "First string {}".format(str1),
#             "\nSecond string {}".format(str2)
#             )
# lst1 = []
# n1 = int(input("How many elements u wanna be in first list? "))
# for i in range(0, n1):
#     ele = input("Input {} info: ".format(i+1))
#     lst1.append(ele)
# lst2 = []
# n2 = int(input("How many elements u wanna be in second list? "))
# for i in range(0, n2):
#     ele2 = input("Input {} info: ".format(i+1))
#     lst2.append(ele2)
# lists_append = MyList(lst1,lst2,2)
# lists_append.returnit()
# lists_append.intostr()
# #---------------------------------------------------- </1> ----------------------------------------------------#



#---------------------------------------------------- <2> ----------------------------------------------------#
class Testpaper:
    def __init__(self, subject, mark_scheme, pass_mark):
        self._subject = subject
        self._mark_scheme = mark_scheme
        self._pass_mark = pass_mark
class Student:
    def __init__(self, student_subject, test_answers):
        self._test_answers = test_answers
        self._student_subject = student_subject
teacher_subject = "math"
teacher_mark_scheme = ['a','a']
teacher_pass_mark = 80
test_teacher = Testpaper(teacher_subject, teacher_mark_scheme, teacher_pass_mark)

student_subject = "math"
student_test_answers = ['a','b']
test_student = Student(student_subject, student_test_answers)

def check_answers(student_test_answers, teacher_mark_scheme):
    return [element for element in student_test_answers if element in teacher_mark_scheme]
check_answers(student_test_answers,teacher_mark_scheme)
# #---------------------------------------------------- </2> ----------------------------------------------------#