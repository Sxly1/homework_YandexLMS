class ShoppingList:
    def __init__(self, *args):
        self.data = []
        for i in range(len(args)):
            self.data.append(list(args[i]))

    def append(self, item):
        self.data.append([item, False])

    def check(self, item):
        for i in range(len(self.data)):
            if self.data[i][0] == item:
                self.data[i][1] = True
                break

    def values(self):
        a = []
        for i in self.data:
            a.append(tuple(i))
        return a

    def checked_values(self):
        a = []
        for i in self.data:
            if i[1]:
                a.append(tuple(i))
        return a

    def rest_values(self):
        a = []
        for i in self.data:
            if not i[1]:
                a.append(tuple(i))
        return a


class TODOList:
    def __init__(self, *args):
        self.data = []
        for i in range(len(args)):
            self.data.append(list(args[i]))
            self.sort()

    def append(self, value, urgency):
        self.data.append([value, urgency, False])
        self.sort()

    def check(self, value):
        for element in self.data:
            if element[0] == value:
                element[2] = True
                break

    def values(self):
        a = []
        for i in self.data:
            a.append(tuple(i))
        return a

    def checked_values(self):
        a = []
        for i in self.data:
            if i[2]:
                a.append(tuple(i))
        return a

    def rest_values(self):
        a = []
        for i in self.data:
            if not i[2]:
                a.append(tuple(i))
        return a

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(n - 1):
                if self.data[j][1] < self.data[j + 1][1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]


class Route:
    def __init__(self, *args):
        self.data = []
        for i in range(len(args)):
            self.data.append(list(args[i]))

    def append(self, station_name, time):
        if not self.data:
            self.data.append([station_name, time, False])
        if self.data[-1][1][:2] * 60 + self.data[-1][1][3:] < time[:2] * 60 + time[3:]:
            self.data.append([station_name, time, False])

    def check(self, value):
        for element in self.data:
            if element[0] == value:
                element[2] = True
                break

    def values(self):
        a = []
        for i in self.data:
            a.append(tuple(i))
        return a

    def checked_values(self):
        a = []
        for i in self.data:
            if i[2]:
                a.append(tuple(i))
        return a

    def rest_values(self):
        a = []
        for i in self.data:
            if not i[2]:
                a.append(tuple(i))
        return a