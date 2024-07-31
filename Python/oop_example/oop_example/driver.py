

class driver():

    def __init__(self,license_level):
        self.license_level = license_level

    def print_speed(self,speed):
        if(speed>80):
            print('the driver speed is too high')

        else:
            print('speed is in legal range')

    def print_distance(self,speed,time):
        distance = speed * time
        print(f'the distance of driving is {distance}')