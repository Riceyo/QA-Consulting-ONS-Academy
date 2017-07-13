class classname:
    def message(self):
        print("hello my friends")
        self.add(7, 2)

    def add(self, a, b):
        print(a + b)

ref = classname()
ref.message()
