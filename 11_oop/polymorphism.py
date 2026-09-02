class student:
    def __init__(self):
        self.x= "hai"
class teacher(student):
    def __init__(self):
        super().__init__()
        self.y= "welcome"
    def display(self):
        print(self.x+"\t"+self.y)
t=teacher()
t.display()
