class Lkh():
    def __init__(self,l,w):
        self.width = w;
        self.len = l;
    def print(self):
        print("""{} love {}""".format(self.width,self.len));
who = Lkh(1,2)
print(who.print())
