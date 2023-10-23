def safe_print_integer(value):
  '''Prints an integer using "{:d}".format().

  Args:
    value: The value to print.

  Returns:
    True if the value is an integer and has been correctly printed, False otherwise.
  '''

  try:
    print("{:d}".format(value))
    return True
  except (TypeError, ValueError):
    return False

