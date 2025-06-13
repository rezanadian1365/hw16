class make_looper:

    def __init__(self, st):
        self.st = st
        self.index = 0

    def __call__(self):
        char = self.st[self.index]
        self.index = ((self.index)+1) % (len(self.st))
        print(char)


abc = make_looper('abc')
abc()   #a
abc()   #b
abc()   #c
abc()