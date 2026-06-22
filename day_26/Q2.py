class vote:
    def __init__(self,age):
        self.age= age

    def person(self):
        if self.age>18:
            print("congratulation ! you are eligible")
        elif self.age<18:
            print("oops! you are under age")
        else:
            print(" you are at borader age")

obj = vote(21)
p = obj.person()
print(p)
        