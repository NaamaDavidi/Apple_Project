
class utils():

    # example of function that getting parameters and return variable
    def summery_calc(num1,mum2):
        summery = num1+mum2
        print(f'sumerry found the value is {summery}')
        if (summery>0):
            print(f'the summery of {num1} and {num2} is higher than 0')
        return summery

    #example of function that getting parameters only
    def print_string(string_to_print):
        print(string_to_print)

    #example of function that is not getting any perameters or return variable
    def print_hello():
        print('hello')

    def fins_len_of_word(word,word2 = 'demo'):
        length = len(word)
        print(f'action at find_length_of_word done the length id {length}')
        if (length<10):
            word = word+'_suffix'
            print(f'the updated word is {word}')
            return  length
        return length