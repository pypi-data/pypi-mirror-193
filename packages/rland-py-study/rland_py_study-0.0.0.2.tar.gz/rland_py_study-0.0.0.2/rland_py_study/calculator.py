class Calculator:
    def __init__(self):
        self._result = 0
    def add(self, num):
        self._result += num
        return self._result
    def sub(self, num):
        self._result -= num
        return self._result
    def mul(self, num):
        self._result *= num
        return self._result
    def div(self, num):
        if num == 0:
            print("Wrong input")
        else:
            self._result /= num
            return self._result
    def result(self):
        return self._result
    def reset(self):
        self._result = 0
        return self._result