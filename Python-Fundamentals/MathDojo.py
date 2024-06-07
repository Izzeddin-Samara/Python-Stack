class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

# create an instance:
md = MathDojo()

# Test case 1:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # output 5

# Test case 2:
md.result = 0
y = md.add(10).subtract(4).add(1, 2, 3).subtract(2, 3, 4).result
print(y)  # output 3

# Test case 3:
md.result = 0
z = md.add(5).subtract(1).add(2, 2).subtract(1, 1, 1).result
print(z)  # output 5


