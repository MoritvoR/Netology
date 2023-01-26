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

    def _print_assessment(self):
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
               'Завершенные курсы: %s' %\
               (self.name, self.surname, self._print_assessment(),
                self._print_courses(), self._print_complete()
                )


class Mentors:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturers(Mentors):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.assessments = {}


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


best_student = Students('Vasia', 'Pupkin')
best_student.courses += ['Python', 'Git', 'API']
best_student.complete_courses += ['Turning on the computer']

suck_student = Students('Some', 'Budy')
suck_student.courses += ['Git', 'Python', 'API']
suck_student.complete_courses += ['Turning on the computer']

cool_lector = Lecturers('Once', 'Toldme')
suck_lector = Lecturers('The', 'World')

cool_reviewer = Reviewers('Is', 'Gonna')
suck_reviewer = Reviewers('Roll', 'Me')

cool_reviewer.courses_attached += ['Python', 'Git', 'API', 'Turning on the computer']
suck_reviewer.courses_attached += ['Python', 'Git', 'API', 'Turning on the computer']

cool_lector.courses_attached += ['Python', 'Git', 'API', 'Turning on the computer']
suck_lector.courses_attached += ['Python', 'Git', 'API', 'Turning on the computer']

cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'API', 10)
print(best_student)

