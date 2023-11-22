class Robot:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.moves = [(self.x, self.y)]

    def move(self, direction):
        for i in direction:
            if i == "N":
                self.y += 1
            if i == "S":
                self.y -= 1
            if i == "E":
                self.x += 1
            if i == "W":
                self.x -= 1
            self.moves.append((self.x, self.y))

        return (self.x, self.y)

    def path(self):
        self.new_moves = self.moves
        self.moves = [self.new_moves[-1]]
        return self.new_moves