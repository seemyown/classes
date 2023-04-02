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
 
