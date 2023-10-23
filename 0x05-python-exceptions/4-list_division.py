#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(0, list_length):
        try:
            results = my_list_1[i] / my_list_2[i]
        except TypeError:
            results = 0
            print("wrong type")
        except ZeroDivisionError:
            results = 0
            print("division by 0")
        except IndexError:
            results = 0
            print("out of range")
        finally:
            pass
        new_list.append(results)
    return (new_list)
