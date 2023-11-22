class Inversion:
    name = "Inversion"

    def solve(self, num):
        return not num

    def truth_table(self):
        print("X\tF")
        for i in range(2):
            print(f"{i}\t{int(not i)}")


class Conjunction:
    name = "Conjunction"

    def solve(self, num1, num2):
        return num1 and num2

    def truth_table(self):
        print("X\tY\tF")
        for i in range(2):
            for y in range(2):
                print(f"{i}\t{y}\t{int(i and y)}")


class Disjunction:
    name = "Disjunction"

    def solve(self, num1, num2):
        return num1 or num2

    def truth_table(self):
        print("X\tY\tF")
        for i in range(2):
            for y in range(2):
                print(f"{i}\t{y}\t{int(i or y)}")


def info(func):
    print(f"Truth table of {func.name}:")
    func.truth_table()