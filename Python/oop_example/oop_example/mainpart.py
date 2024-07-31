from Python.oop_example.oop_example.driver import driver
from Python.oop_example.oop_example.lecture import lecture
from Python.oop_example.oop_example.student import student


class mainpart():
    print('test start')
    lecture_history = lecture()
    lecture_English = lecture ()
    student_1 = student('johan','smith')
    student_2 = student ('haim','cohen')
    driver_1 = driver('a')

    driver_1.print_speed(60)
    student_1.age_cal(23)
    student_2.age_cal(21)
    student_1.avarage_calc([67,37,90,100])

    student_1.age_prining_into_person(34)


    print('test end')