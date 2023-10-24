#include <Python.h>
#include <stdio.h>
#define PY_SSIZE_T_MAX ((Py_ssize_t)(((size_t)-1)>>1))

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - print information about plyfloatobject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t a, size;
    PyObject *item;
    size = PyList_GET_SIZE(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (a = 0; a < size; a++)
    {
        item = PyList_GET_ITEM(p, a);
        printf("Element %ld: %s\n", a, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t a, size;
    char *str;
    size = ((PyVarObject *)p)->ob_size;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

    if (size > 10)
        size = 10;

    str = ((PyBytesObject *)p)->ob_sval;
    printf("  first %ld bytes: ", size);
    for (a = 0; a < size; a++)
    {
        printf("%02hhx", str[a]);
        if (a < size - 1)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}
