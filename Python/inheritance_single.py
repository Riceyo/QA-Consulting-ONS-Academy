class empty:
    pass
class parent:
    def printparent(self):
        print("parent")
class child(parent):
    def printchild(self):
        print("child")
class grandchild(child):
    def printgrandchild(self):
        print("grandchild")
        print(issubclass(grandchild, child))  # check if sub class
        print(issubclass(grandchild, parent))  # check if sub class
        print(issubclass(child, parent))  # check if sub class
        print(issubclass(parent, child))  # check if sub class
        super(grandchild, self).printchild()  # not naming inherit class
        super(grandchild, self).printparent()  # not naming inherit class
        child.printchild(self)  # same but specify class
        parent.printparent(self)  # same but specify class
        child.printparent(self)  # child has inherited parent


blah = grandchild()
blah.printparent()
blah.printchild()
blah.printgrandchild()
empty = empty()

print(isinstance(blah, grandchild))  # check if object in class
print(isinstance(blah, child))  # check if object in class
print(isinstance(blah, parent))  # check if object in class
print(isinstance(empty, grandchild))  # check if object in class