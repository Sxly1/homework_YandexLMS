class Wardrobe:
    def __init__(self, *args):
        self.arr = list([_ for _ in args])
        self.type = -1

    def __str__(self):
        s = ""
        for i in self.arr:
            s += i + " "
        r = s[:-1]
        return r

    def __eq__(self, other):
        if self.type == other.type:
            return len(self.arr) == len(other.arr)
        else:
            return self.type == other.type

    def __ne__(self, other):
        if self.type == other.type:
            return len(self.arr) != len(other.arr)
        else:
            return self.type != other.type

    def __lt__(self, other):
        if self.type == other.type:
            return len(self.arr) < len(other.arr)
        else:
            return self.type < other.type

    def __gt__(self, other):
        if self.type == other.type:
            return len(self.arr) > len(other.arr)
        else:
            return self.type > other.type

    def __le__(self, other):
        if self.type == other.type:
            return len(self.arr) <= len(other.arr)
        else:
            return self.type <= other.type

    def __ge__(self, other):
        if self.type == other.type:
            return len(self.arr) >= len(other.arr)
        else:
            return self.type >= other.type


class JustWardrobe(Wardrobe):
    def __init__(self, *args):
        self.arr = list([_ for _ in args])
        self.type = 0

    def __str__(self):
        s = ""
        for i in self.arr:
            s += i + ", "
        r = s[:-2] + "."
        return r.capitalize()


class MagicWardrobe(Wardrobe):
    def __init__(self, *args):
        self.arr = list([_ for _ in args])
        self.type = 1

    def __str__(self):
        self.arr.sort()
        for i in range(len(self.arr)):
            self.arr[i] = self.arr[i].capitalize()

        s = ""
        for i in self.arr:
            s += i + ", "
        r = s[:-2] + "."
        return r