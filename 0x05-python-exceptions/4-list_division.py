#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
        my_list_1 (list): first list containing the dividends.
        my_list_2 (list): second list containing the divisors to be matched.
                            with my_list_1 at equal indexes.
        list_length: length of lists.

    Returns:
        A new list with (length= list_length).
    """
    new_list = []
    for i in range(list_length):
        a = 0
        try:
            a = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(float(a) if a else 0)

    return (new_list)
