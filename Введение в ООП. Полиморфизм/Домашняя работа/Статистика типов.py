class TypeStatistics:
    def __init__(self, arr):
        self.arr = arr
        self.s = {}
        self.scount = {}

    def type_values(self):

        for i in self.arr:
            typ = type(i)
            endindex = 0
            for j in range(8, len(str(typ)) + 1):
                if str(typ)[j] == "'":
                    endindex = j
                    break
            typ = str(type(i))[8:endindex]
            if typ not in self.s:
                self.s[typ] = [i]
                self.scount[typ] = 1
            else:
                self.s[typ].append(i)
                self.scount[typ] += 1
        return self.s

    def type_counts(self):
        return self.scount