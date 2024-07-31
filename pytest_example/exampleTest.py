import unittest


class PyTestExample(unittest.TestCase):

    def test_1(self):
        pw = 'wewewewewe'
        print('into test 1')
        assert len(pw)==10 , 'the length of pw is not as expected'


    def test_2(self):

        print('into test 2')
        assert 1==2 , '1 in not 1 as exepcted'


    def test_summery(self):
        num1= 1
        num2 =2
        sum = num1+num2
        assert sum ==3, 'the summery of num1 and num2 is not as expected'