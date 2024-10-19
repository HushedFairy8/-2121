class student:
    print("hi")
    def __init__(self, height=160):
     self.height = height
     print('i am alive')

first_student = student()
second_student = student(height=170)
print(first_student.height)
print(second_student.height)