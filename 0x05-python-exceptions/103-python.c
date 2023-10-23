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
