class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university
        self.year = 1

    def get_name(self):
        return self.name

    def get_university(self):
        return self.university

    def get_year(self):
        return self.year

    def study(self):
        if self.year == 6:
            return self.year
        else:
            self.year += 1
            return self.year


class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        self.position = 1

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def get_position(self):
        if self.position == 1:
            return "junior"
        if self.position == 2:
            return "middle"
        if self.position == 3:
            return "senior"
        else:
            return "lead"

    def work(self):
        self.position += 1


class Human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name