class archaea(object):
    def metabolise(self):
        print("archaea metabolise")
class fish(archaea):
    def swim(self):
        print("fish swim")
    def breathe(self):
        print("fish breathe")
class reptile(archaea):
    def walk(self):
        print("reptile walk")
    def breathe(self):
        print("reptile breathe")
class amphibian(reptile, fish):  # takes left parameter first for same name methods
    pass

amp = amphibian()
amp.swim()
amp.walk()
amp.breathe()