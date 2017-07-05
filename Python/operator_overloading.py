class mathoverload:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    def __add__(self, right):
        defadd = mathoverload(0, 0, 0)
        defadd.a = self.a + right.a
        defadd.b = self.b + right.b
        defadd.c = self.c + right.c
        return defadd
    def __sub__(self, right):
        defsub = mathoverload(0, 0, 0)
        defsub.a = self.a - right.a
        defsub.b = self.b - right.b
        defsub.c = self.c - right.c
        return defsub
    def __str__(self):
        return str(self.a) + ", " + str(self.b) + ", " + str(self.c)

objref1 = mathoverload(1, 2, 3)
objref2 = mathoverload(1, 2, 3)
mathoverloadadd = objref1 + objref2
print(mathoverloadadd)
mathoverloadsub = objref1 - objref2
print(mathoverloadsub)
