class Student:
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark  # 1-5

    def getscholarship(self):
        if self.averageMark == 5:
            return f'Stupendiya studenta {self.firstName} {self.lastName} - 100 uah'
        elif self.averageMark == 4 or self.averageMark == 3 or \
                self.averageMark == 2 or self.averageMark == 1:
            return f'Stupendiya studenta {self.firstName} {self.lastName} - 80 uah'
        else:
            return f'Nepravilnaya ochenka'


class Aspirant(Student):
    def __init__(self, firstName, lastName, group, averageMark, scientificWork):
        super().__init__(firstName, lastName, group, averageMark)
        self.scientificWork = scientificWork

    def getscholarship(self):
        if self.averageMark == 5:
            return f'Stupendiya studenta {self.firstName} {self.lastName} - 200 uah'
        elif self.averageMark == 4 or self.averageMark == 3 or \
                self.averageMark == 2 or self.averageMark == 1:
            return f'Stupendiya studenta {self.firstName} {self.lastName} - 180 uah'
        else:
            return f'Nepravilnaya ochenka'


s1 = Student('Masha', 'Pupkina', '4A', 5)
s1.getscholarship()
s2 = Student('Pasha', 'Pipkin', '4B', 4)
s2.getscholarship()
s3 = Aspirant(Student)('Sasha', 'Pepkin', '5A', 5, 1)
s3.getscholarship()
