class Holiday:
    def __init__(self, name, date):
        self.classn = "Holiday"
        self.name = name
        self.day = date.split()[0]
        self.month = date.split()[1]

    def get_season(self):
        if self.month in "DecemberJanuaryFebruary":
            return "Winter"
        if self.month in "MarchAprilMay":
            return "Spring"
        if self.month in "JuneJulyAugust":
            return "Summer"
        if self.month in "SeptemberOctoberNovember":
            return "Autumn"

    def __str__(self):
        return f"{self.classn}('{self.name}', '{self.day} {self.month}')"


class NewYear(Holiday):
    def __init__(self, name, date, people):
        self.classn = "NewYear"
        self.name = name
        self.day = date.split()[0]
        self.month = date.split()[1]
        self.arr = people[:]

    def congratulate(self, name):
        if name in self.arr:
            return f"Dear {name}! Happy New Year!"
        else:
            self.arr.append(name)
            return f"Dear new friend {name}! Have fun this New Year!"

    def get_greet(self):
        return self.arr


class MuseumDay(Holiday):
    def __init__(self, name, date, list):
        self.name = name
        self.classn = "MuseumDay"
        self.day = date.split()[0]
        self.month = date.split()[1]
        self.list = list

    def get_museums(self):
        return self.list