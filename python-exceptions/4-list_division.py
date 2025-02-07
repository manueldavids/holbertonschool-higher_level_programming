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
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = num1 / num2
        except (TypeError, ZeroDivisionError, IndexError) as e:
            if isinstance(e, TypeError):
                print("wrong type")
            elif isinstance(e, ZeroDivisionError):
                print("division by 0")
            else:
                print("out of range")
            result = 0
        finally:
            new_list.append(result)

    return new_list
