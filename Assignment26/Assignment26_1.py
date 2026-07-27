class Demo:
    #class variables
    Value1 = 10

    #constructor
    def __init__(self,No1,No2):
        self.No1 = 11  #instance variable
        self.No2 = 22

    #instance Method-can access both instance var and class var
    def fun(self):
        print("Inside Instance method:fun")
        print("self.No1",self.No1)
        print("self.No2",self.No2)

    def gun(self):
        print("Inside Instance method:gun")
        print("self.No1",self.No1)
        print("self.No2",self.No2)
    

Dobj1 = Demo(11,21)
Dobj2 = Demo(51,101)

Dobj1.fun()
Dobj2.gun()
Dobj1.fun()
Dobj2.gun()
