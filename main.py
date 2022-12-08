
stud_list = []
lect_list = []

def student_average(list, cource):
    grade, quantity = 0, 0
    for a in list:
        if cource in a.courses_in_progress:
            grade += Student.average(Student, a.grades)
            quantity +=1
    if quantity:
        agrade = grade / quantity
        print(f"Средняя оценка студентов курса {cource} = {agrade}")
    else:
        print(f"Наши студенты сейчас не проходят курс {cource}.")
    return

def lecturer_average(list, cource):
    grade, quantity = 0, 0
    for a in list:
        if cource in a.courses_attached:
            grade += Student.average(Lecturer, a.grades)
            quantity +=1
    if quantity:
        agrade = grade / quantity
        print(f"Средний рейтинг лекторов курса {cource} = {agrade}")
    else:
        print(f"Наши лекторы сейчас не читают курс {cource}.")
    return

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.reg()

    def reg(self):
        stud_list.append(self)
        return
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_courses(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self, grades):
        grades_list = [n for grade in grades.values() for n in grade]
        if grades_list:
          result =  sum(grades_list) / len(grades_list)
        return result

    def __str__(self):
        middle = self.average(self.grades)
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:"\
                f"{round(middle, 1)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"\
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        return res

    def __lt__(self, other):
        if self.average(self.grades) > other.average(other.grades):
            print(f"Студент {self.name} {self.surname} учится лучше студента {other.name} {other.surname}")
            return
        elif self.average(self.grades) < other.average(other.grades):
            print(f"Студент {self.name} {self.surname} учится хуже студента {other.name} {other.surname}")
            return
        elif self.average(self.grades) == other.average(other.grades):
            print(f"Студент {self.name} {self.surname} учится также как и студент {other.name} {other.surname}")
            return

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.reg()
    def reg(self):
        lect_list.append(self)
        return

    def __str__(self):
        middle = Student.average(self, self.grades)
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(middle, 1)}\n"
        return res

    def __lt__(self, other):
        if Student.average(self, self.grades) > Student.average(self, other.grades):
            print(f"Лектор {self.name} {self.surname} имеет рейтинг лучше лектора {other.name} {other.surname}")
            return
        elif Student.average(self, self.grades) < Student.average(self, other.grades):
            print(f"Лектор {self.name} {self.surname} имеет рейтинг хуже лектора {other.name} {other.surname}")
            return
        elif Student.average(self, self.grades) == Student.average(self, other.grades):
            print(f"Лектор {self.name} {self.surname} имеет такойже рейтинг, как и лектор {other.name} {other.surname}")
            return
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

luser_student = Student('Test', 'Test', 'your_gender')
luser_student.courses_in_progress += ['Python']

best_reviewer = Reviewer('Some', 'One')
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(luser_student, 'Python', 5)
best_reviewer.rate_hw(luser_student, 'Python', 5)

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Python']

luser_lecturer = Lecturer('test', 'test')
luser_lecturer.courses_attached += ['Python']


best_student.rate_courses(best_lecturer, 'Python', 10)
best_student.rate_courses(best_lecturer, 'Python', 10)
best_student.rate_courses(best_lecturer, 'Python', 10)

best_student.rate_courses(luser_lecturer, 'Python', 7)
best_student.rate_courses(luser_lecturer, 'Python', 7)
best_student.rate_courses(luser_lecturer, 'Python', 7)

print(luser_student)
print(best_student)
luser_student > best_student


student_average(stud_list, "Java")
lecturer_average(lect_list, "Paython")