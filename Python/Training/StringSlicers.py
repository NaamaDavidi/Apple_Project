class StringSlicers():
    string_for_demo = 'hello world'
    string_with_numbers = '323232'
    slice_from_begin = string_for_demo [:5]
    print(slice_from_begin)
    slice_to_end = string_for_demo[6:]
    print(slice_to_end)
    slice_middle = string_for_demo[5:7]
    print(slice_middle)
    slice_to_end_1 = string_for_demo[-3:]
    print(slice_to_end_1)
    index = string_for_demo.index(' ')
    slice_index_example = string_for_demo[index:]
    counter_l = string_for_demo.count('l') # count the number of l into string_for_demo
    sub = 'world'
    in_num = string_for_demo.isalnum()
    # string_for_demo = string_with_numbers.replace(_old=";hi"._new='hi')
    print('test end')