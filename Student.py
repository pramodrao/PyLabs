from Person import Person


class Student(Person):

    last_id = 0

    def __init__(self, name):
        Person.__init__(self, name)
        Student.last_id += 1
        self.id = Student.last_id
        self.standard = None

    def get_id(self):
        return self.id

    def get_standard(self):
        return self.standard

    def set_standard(self, standard):
        self.standard = standard

    def __lt__(self, other):
        return self.id < other.id
