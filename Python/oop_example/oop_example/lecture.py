from Python.oop_example.oop_example.person import person


class lecture(person):
    def __init__(self,type):
        self.type = type

    def tax_cal(self,salary,tax=30):
        salary_last = salary*(100-tax)/100
        return salary