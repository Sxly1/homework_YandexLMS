vowels = "eyuioa"


class Knight:
    def __init__(self, *args):
        self.name = args[0]
        self.weapons = args[1:]

    def fight(self, weapon):
        if weapon not in self.weapons:
            return "None"
        sound = ""
        for i in weapon:
            if i not in vowels:
                sound += i
        return sound.upper()

    def info(self):
        return f"Knight({self.name})"

    def announce(self, lady):
        return f"Long live the noblest {lady}!"


class Squire:
    def __init__(self, *args):
        self.name = args[0]
        self.knight_name = args[1]
        self.weapons = args[2:]

    def fight(self, weapon):
        if weapon not in self.weapons:
            return "None"
        sound = ""
        for i in weapon:
            if i not in vowels:
                sound += i
        return sound.lower()

    def info(self):
        return f"Squire({self.name})"

    def praise(self):
        return f"Glory to {self.knight_name}!"