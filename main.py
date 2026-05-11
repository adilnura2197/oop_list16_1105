class Teacher:
    def __init__(self, ism):
        self.ism = ism


class School:
    def __init__(self):
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher.ism)

    def show(self):
        print(self.teachers)


t1 = Teacher("Aziza")
t2 = Teacher("Sardor")

s1 = School()
s1.add_teacher(t1)
s1.add_teacher(t2)
s1.show()
