def funct(x):
    if int(x) == 1:
        def functnest(nestvar1, nestvar2):
            print("funcnest x1")
        return functnest
    if int(x) == 2:
        def functnest(nestvar1, nestvar2):
            print("funcnest x2")
        return functnest


blah = funct(1)
blah('abc', 'xyz')

blah = funct(2)
blah('abc', 'xyz')