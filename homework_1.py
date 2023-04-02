class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average(self):
        averages = []
        for key, val in self.grades.items():
            average = sum(val)/len(val)
            averages.append(average)
        total_avr = sum(averages)/len(averages)   
        return total_avr   
    

    def __str__(self):
        self.cour_in_p = ', '.join(map(str,self.courses_in_progress))
        self.fin_cour = ', '.join(map(str,self.finished_courses))
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average()}\nКурсы в процессе изучения: {self.cour_in_p}\nЗавершенные курсы: {self.fin_cour}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average() < other.average()
            
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
         
class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        
    def average(self):
        averages = []
        for key, val in self.grades.items():
            average = sum(val)/len(val)
            averages.append(average)
        total_avr = sum(averages)/len(averages)   
        return total_avr         

     
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}'
    
    def __lt__(self, other):
        if isinstance(other, Lecture):
            return self.average() < other.average()
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'
 

def aversge_grade_students(students_list, course):
    grades = []
    for student in students_list:
        if course in student.courses_in_progress:
            grades.append(student.average())
    return f'Средняя оценка студентов по курсу "{course}": {sum(grades)/len(grades)}'

def aversge_grade_lectures(lectures_list, course):
    grades = []
    for lecture in lectures_list:
        if course in lecture.courses_attached:
            grades.append(lecture.average())
    return f'Средняя оценка лекторов по курсу "{course}": {sum(grades)/len(grades)}'


student_1 = Student('Pol', 'Doll', 'male')
student_2 = Student('Kate', 'Rill', 'female')
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python']

lecture_1 = Lecture('Dmitriy', 'Corush')
lecture_2 = Lecture('Anna', 'Dell')
lecture_1.courses_attached += ['Python']
lecture_2.courses_attached += ['Python']

student_1.grade_lecture(lecture_1, 'Python', 10)
student_2.grade_lecture(lecture_1, 'Python', 9)
student_1.grade_lecture(lecture_1, 'Python', 9)
student_2.grade_lecture(lecture_1, 'Python', 10)

student_1.grade_lecture(lecture_2, 'Python', 10)
student_2.grade_lecture(lecture_2, 'Python', 9)
student_1.grade_lecture(lecture_2, 'Python', 9)
student_2.grade_lecture(lecture_2, 'Python', 10)

reviewer_1 = Reviewer('Leo', 'Dicaprio')
reviewer_2 = Reviewer('Jack', 'Sparrow')
reviewer_1.courses_attached += ['Python', 'Java']
reviewer_2.courses_attached += ['Java', 'Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)

stud_list = []
stud_list.append(student_1)
stud_list.append(student_2)

lecture_list = []
lecture_list.append(lecture_1)
lecture_list.append(lecture_2)

print(aversge_grade_students(stud_list, 'Python'))
print(aversge_grade_lectures(lecture_list, 'Python'))
