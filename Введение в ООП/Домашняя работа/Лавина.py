class Avalanche:
    def __init__(self):
        self.isFirst = True
        self.string = "O"

    def go(self):
        if self.isFirst:
            print("O")
            self.isFirst = False
        else:
            self.string = self.string.replace("O", "*")
            self.string = self.string.replace("o", "-")
            self.string = self.string.replace("-", "oOo")
            self.string = self.string.replace("*", "ooOoo")
            print(self.string)