class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def sayFirstName(self):
        print("Печать имени", self.first_name)
    def sayLastName(self):
        print("Печать фамилии", self.last_name)
    def writeAll(self):
        print("Всё вместе", self.first_name, self.last_name)
    