import datetime
from dateutil.relativedelta import relativedelta


class Person(object):

    def __init__(self, name):
        self.name = name
        try:
            p = name.rindex(' ')
            self.lastName = name[p+1:]
        except IOError:
            self.lastName = name
        self.birthdate = None

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.lastName

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def get_age(self, in_days):
        if self.birthdate is None:
            raise ValueError
        age = relativedelta(datetime.date.today(), self.birthdate)

        if in_days:
            return str(age.days) + ' days'

        return str(age.years) + ' years and ' + str(age.months) + ' months'

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

