#!/usr/bin/python3
"""Prints x elements of a list, on the same line followed by a new line.

  Args:
    my_list: A list of any type of elements.
    x: The number of elements to print.

  Returns:
    The real number of elements printed.
  """
def safe_print_list(my_list=[], x=0):
    c = 0
    for m in range(x):
        try:
            print(my_list[m], end="")
            c += 1
        except IndexError:
            break
    print()
    return c
