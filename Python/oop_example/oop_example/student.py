from Python.oop_example.oop_example.person import person

class student (person):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def avarage_calc(self,grades):
        summery = 0
        for grade in grades:
           summery = summery + grade

        grades_size = len(grades)
        avarege = summery/grades_size
        print(f'the avarage grades is {avarege}')
        return avarege

