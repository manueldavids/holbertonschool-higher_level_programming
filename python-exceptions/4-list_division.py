#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element 2 lists.

    Args:
        my_list_1: First list containing elements.
        my_list_2: Second list containing elements.
        list_length: The number of elements to divide.

    Returns:
        A new list with the results of the divisions.
    """
    new_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
                result = 0
            else:
                result = a / b
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
