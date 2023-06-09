#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for items in range(list_length):
        divide = 0
        try:
            divide = my_list_1[items] / my_list_2[items]
        except (ZeroDivisionError):
            print('division by 0')
        except (TypeError):
            print('wrong type')
        except (IndexError):
            print('out of range')
        finally:
            new_list.append(divide)
    return (new_list)
