#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - prints python string
 * @p: python object
 *
 * Return: no return
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *repr;

	(void)repr;
	printf("[.] string object info\n");
}
