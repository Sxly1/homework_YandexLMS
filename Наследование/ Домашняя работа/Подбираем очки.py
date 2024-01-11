class Glasses:
    def __init__(self, mode=1, dist=64, sun=False, d=0):
        self.mode = mode
        self.dist = dist
        self.sun = sun
        self.d = d

    def __str__(self):
        return f"{self.__class__.__name__}({self.mode}, {self.dist}, {self.sun}, {self.d})"

    def focus(self):
        if self.d == 0:
            return "inf"
        return round(100 / self.d, 1)


class NearSightedNess(Glasses):
    def __init__(self, mode=1, dist=64, sun=False, dl=0, dr=0):
        self.mode = mode
        self.dist = dist
        self.sun = sun
        self.dl = dl
        self.dr = dr
        if abs(dl) > abs(dr):
            self.d = dl
        else:
            self.d = dr

    def __str__(self):
        return f"{self.__class__.__name__}({self.mode}, {self.dist}, {self.sun}, {max(abs(self.dr), abs(self.dl))})"

    def best_vision_distance(self):
        if max(abs(self.dl), abs(self.dr)) == 0:
            return "inf"
        return round(100 / max(abs(self.dl), abs(self.dr)), 1)


class FarSightedNess(Glasses):
    def __init__(self, mode=1, dist=64, sun=False, dl=0, dr=0):
        self.mode = mode
        self.dist = dist
        self.sun = sun
        self.dl = dl
        self.dr = dr
        if abs(dl) > abs(dr):
            self.d = dl
        else:
            self.d = dr

    def __str__(self):
        return f"{self.__class__.__name__}({self.mode}, {self.dist}, {self.sun}, {max(self.dl, self.dr)})"

    def best_vision_distance(self):
        if max(abs(self.dl), abs(self.dr)) == 0:
            return "inf"
        return round(100 / max(abs(self.dl), abs(self.dr)), 1)