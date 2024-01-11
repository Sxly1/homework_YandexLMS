trigger = ":;"


class Liked:
    def __init__(self, *args):
        self.arr = list([_ for _ in args])
        self.s = {}

    def checklikes(self):
        for string in self.arr:
            flag = False
            for elem in range(len(string)):
                if not flag:
                    if string[elem] in trigger:
                        flag = True
                        s = string[elem] + string[elem + 1]
                        if s in self.s:
                            self.s[string[elem] + string[elem + 1]] += 1
                        else:
                            self.s[string[elem] + string[elem + 1]] = 1
                    elif string[elem] in "()":
                        if string[elem] in self.s:
                            self.s[string[elem]] += 1
                        else:
                            self.s[string[elem]] = 1
                else:
                    flag = False

    def likes(self):
        self.checklikes()
        return self.s


class MiMiMi(Liked):
    def __init__(self, *args):
        self.arr = list([_ for _ in args])
        self.s = {}

    def checklikes(self):
        for string in self.arr:
            flag = False
            for elem in range(len(string)):
                if not flag and ("cat" in string or "kitten" in string):
                    if string[elem] in trigger:
                        flag = True
                        s = string[elem] + string[elem + 1]
                        if s in self.s:
                            self.s[string[elem] + string[elem + 1]] += 1
                        else:
                            self.s[string[elem] + string[elem + 1]] = 1
                    elif string[elem] in "()":
                        if string[elem] in self.s:
                            self.s[string[elem]] += 1
                        else:
                            self.s[string[elem]] = 1
                else:
                    flag = False