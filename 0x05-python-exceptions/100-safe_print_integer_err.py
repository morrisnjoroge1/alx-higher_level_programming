#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
  """Prints an integer, or returns False and prints the error to stderr otherwise.

  Args:
    value: The value to print.

  Returns:
    True if the value is an integer, False otherwise.
  """
      try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
