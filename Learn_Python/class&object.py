class Human:
    def __init__(self,n, o):
        self.name = n
        self.occupation = o


    def do_work(self):
        print(self.name)
        print(self.occupation)

    def speak(self):
        print(self.name,"speaking english")

Tom = Human("Tom",'Actor')
Tom.do_work()
Tom.speak()



