from Person import Person


class Teacher(Person):

    last_id = 0

    def __init__(self, name):
        Person.__init__(self, name)
        Teacher.last_id += 1
        self.id = Teacher.last_id
        self.designation = None

    def get_id(self):
        return self.id

    def get_designation(self):
        return self.designation

    def set_designation(self, designation):
        self.designation = designation

    def __lt__(self, other):
        return self.id < other.id
