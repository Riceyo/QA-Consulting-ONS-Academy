class results:
    def __init__(self, a=0, b=0, c=0):
        self.__phy = a
        self.__che = b
        self.__mat = c
        self.__passcount = 0
        self.__defphy(self.__phy)
        self.__defphy(self.__che)
        self.__defphy(self.__mat)
        self.__calc()
        self.__display()
    def __defphy(self, phy):
        if phy > 0 and phy < 101:
            phy = phy
        else:
            print("phy invalid")
        if phy > 69:
            self.__passcount = self.__passcount + 1
    def __defche(self, che):
        if che > 0 and che < 101:
            che = che
        else:
            print("che invalid")
        if che > 69:
            self.__passcount = self.__passcount + 1
    def __defmat(self, mat):
        if mat > 0 and mat < 101:
            mat = mat
        else:
            print("mat invalid")
        if mat > 69:
            self.__passcount = self.__passcount + 1
    def __calc(self):
        self.__total = self.__phy + self.__che + self.__mat
        self.__per = self.__total * 100 / 300
    def __display(self):
        print(self.__total)
        print(self.__per)
        if self.__passcount == 0:
            print("go home")
        if self.__passcount == 1:
            print("retake course")
        if self.__passcount == 2:
            print("retake exam")

richmond = results(69, 69, 69)
