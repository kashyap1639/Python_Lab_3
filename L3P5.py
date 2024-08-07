class Calculator:
    def __init__(self):
        self.__result = 0
    def add(self,_a,_b):
        self._a = _a
        self._b = _b
        self.__result = self._a + self._b
        print(self.__result)
    def sub(self,_a,_b):
        self._a = _a
        self._b = _b
        self.__result = self._a - self._b
        print(self.__result)
x = Calculator()
x.add(10,5)
x.sub(10,5)
 