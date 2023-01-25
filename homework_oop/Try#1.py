class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            pass
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    pass


best_student = Student('Vasia', 'Pupkin')
best_student.courses += ['Python', 'Git']
suck_student = Student('Some', 'Budy')
suck_student.courses += ['Git', 'Python']

cool_lector = Lecturer('Once', 'Toldme')
cool_lector.courses_attached += ['Python']
suck_lector = Lecturer('The', 'World')
suck_lector.courses_attached += ['Git']

cool_reviewer = Reviewer('Is', 'Gonna')
cool_reviewer.courses_attached += ['Git']
suck_reviewer = Reviewer('Roll', 'Me')
suck_reviewer.courses_attached += ['Python']

