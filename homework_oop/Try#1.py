class Students:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.complete_courses = []
        self.assessments = {}

    def rate_lector(self, lector,  course: str, assessment: int):
        """Add assessment to the lecturer"""
        if isinstance(lector, Lecturers):
            if course in lector.courses_attached and\
                    course in self.courses:
                lector.assessments[course] = assessment
            else:
                print('Uncorrected course: ', course)
        else:
            print('Fatal error. Please, delete or kill me')

    def _average_rating(self):
        return sum(self.assessments.values()) / len(self.assessments.values())

    def _print_courses(self):
        pr_cour = ''
        for now in self.courses:
            pr_cour = pr_cour + ' ' + str(now)
        return pr_cour

    def _print_complete(self):
        pr_compl = ''
        for now in self.complete_courses:
            pr_compl = pr_compl + ' ' + str(now)
        return pr_compl

    def __str__(self):
        return 'Имя: %s \n' \
               'Фамилия: %s\n' \
               'Средняя оценка за домание задания: %s\n' \
               'Курсы в процессе изучения: %s\n' \
               'Завершенные курсы: %s\n' %\
               (self.name, self.surname, self._average_rating(),
                self._print_courses(), self._print_complete()
                )

    def __eq__(self, other):
        if isinstance(other, Students):
            if self._average_rating() != other._average_rating():
                return False
            else:
                return True
        else:
            print('Fatal error. Uncorrected type.')

    def __lt__(self, other):
        if isinstance(other, Students):
            if self._average_rating() < other._average_rating():
                return True
            else:
                return False
        else:
            print('Fatal error. Uncorrected type.')

    def __le__(self, other):
        if isinstance(other, Students):
            if self._average_rating() <= other._average_rating():
                return True
            else:
                return False
        else:
            print('Fatal error. Uncorrected type.')

    def __ge__(self, other):
        if isinstance(other, Students):
            if self._average_rating() >= other._average_rating():
                return True
            else:
                return False
        else:
            print('Fatal error. Uncorrected type.')


class Mentors:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturers(Mentors):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.assessments = {}

    def _average_rating(self):
        return sum(self.assessments.values()) / len(self.assessments.values())

    def __str__(self):
        return 'Имя: %s \n' \
               'Фамилия: %s\n' \
               'Средняя оценка за лекции: %s\n' % \
               (self.name, self.surname, self._average_rating())

    def __eq__(self, other):
        if isinstance(other, Lecturers):
            if self._average_rating() != other._average_rating():
                return False
            else:
                return True
        else:
            print('Fatal error. Uncorrected type.')

    def __lt__(self, other):
        if isinstance(other, Lecturers):
            if self._average_rating() < other._average_rating():
                return True
            else:
                return False
        else:
            print('Fatal error. Uncorrected type.')

    def __le__(self, other):
        if isinstance(other, Lecturers):
            if self._average_rating() <= other._average_rating():
                return True
            else:
                return False
        else:
            print('Fatal error. Uncorrected type.')

    def __ge__(self, other):
        if isinstance(other, Lecturers):
            if self._average_rating() >= other._average_rating():
                return True
            else:
                return False
        else:
            print('Fatal error. Uncorrected type.')


class Reviewers(Mentors):

    def rate_hw(self, student, course: str, assessment: int):
        """Add assessment to the student"""
        if isinstance(student, Students):
            if course in student.courses and\
                    course in self.courses_attached:
                student.assessments[course] = assessment
            else:
                print('Uncorrected course: ', course)
        else:
            print('Fatal error. Please, delete or kill me')

    def __str__(self):
        return 'Имя: %s \n' \
               'Фамилия: %s\n' % \
               (self.name, self.surname)


def rate_students(students: list, course: str):
    """Average student grade per course"""
    all_sum = 0
    counter = 0
    for now_student in students:
        if course in now_student.assessments:
            all_sum += now_student.assessments[course]
            counter += 1
    return all_sum / counter


def rate_lecturers(lecturers: list, course: str):
    """Average lecturers grade per course"""
    all_sum = 0
    counter = 0
    for now_lector in lecturers:
        if course in now_lector.assessments:
            all_sum += now_lector.assessments[course]
            counter += 1
    return all_sum / counter


best_student = Students('All', 'Star')
suck_student = Students('Some', 'Budy')
cool_lector = Lecturers('Once', 'Toldme')
suck_lector = Lecturers('The', 'World')
cool_reviewer = Reviewers('Is', 'Gonna')
suck_reviewer = Reviewers('Roll', 'Me')

best_student.courses += ['Python', 'Git', 'API']
best_student.complete_courses += ['Turning on the computer']

suck_student.courses += ['Git', 'Python', 'API']
suck_student.complete_courses += ['Turning on the computer']

cool_reviewer.courses_attached += ['Python', 'Git', 'API', 'Turning on the computer']
suck_reviewer.courses_attached += ['Python', 'Git', 'API', 'Turning on the computer']

cool_lector.courses_attached += ['Python', 'Git', 'API', 'Turning on the computer']
suck_lector.courses_attached += ['Python', 'Git', 'API', 'Turning on the computer']

cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(suck_student, 'API', 1)

suck_reviewer.rate_hw(suck_student, 'Python', 4)
suck_reviewer.rate_hw(suck_student, 'Git', 2)
suck_reviewer.rate_hw(best_student, 'API', 10)

best_student.rate_lector(cool_lector, 'Python', 8)
suck_student.rate_lector(cool_lector, 'Git', 9)
best_student.rate_lector(suck_lector, 'API', 2)
suck_student.rate_lector(suck_lector, 'Python', 1)

all_lecturers = [cool_lector, suck_lector]
all_students = [best_student, suck_student]

print(best_student)
print(suck_student)
print(cool_lector)
print(suck_lector)
print(cool_reviewer)
print(suck_reviewer)
print(best_student == suck_student)
print(best_student != suck_student)
print(best_student <= suck_student)
print(best_student >= suck_student)
print(best_student < suck_student)
print(best_student > suck_student)
print(cool_lector == suck_lector)
print(cool_lector != suck_lector)
print(cool_lector <= suck_lector)
print(cool_lector >= suck_lector)
print(cool_lector < suck_lector)
print(cool_lector > suck_lector)
print(rate_students(all_students, 'Python'))
print(rate_lecturers(all_lecturers, 'Git'))
