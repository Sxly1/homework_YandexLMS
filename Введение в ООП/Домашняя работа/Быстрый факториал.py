class QuickFactorial:
    def __init__(self):
        self.nums = []

    def result(self, n):
        for i in range(1, n + 1):
            self.nums.append(i)

        result = 1
        for num in self.nums:
            result *= num

        return result