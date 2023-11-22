class Cabbage:
    def __init__(self, size_highest, step, stalk_size):
        self.size_highest = size_highest
        self.step = step
        self.stalk_size = stalk_size
        self.current_size = size_highest

    def leaf(self):
        if self.current_size - self.step >= self.stalk_size:
            self.current_size -= self.step
        else:
            self.current_size = self.stalk_size
        print(self.current_size)