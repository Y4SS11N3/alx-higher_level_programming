#define _POSIX_C_SOURCE 200809L
#include <time.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Displays basic information about Python byte objects.
 * @p: PyObject pointer representing a Python byte object.
 */
void print_python_bytes(PyObject *p) {
    char *str;
    long int sz, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    sz = ((PyVarObject *)(p))->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", sz);
    printf("  trying string: %s\n", str);

    limit = sz >= 10 ? 10 : sz + 1;
    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++) {
        printf(" %02x", str[i] & 0xff);
    }
    printf("\n");
}

/**
 * print_python_list - Displays basic information about Python lists.
 * @p: PyObject pointer representing a Python list.
 */
void print_python_list(PyObject *p) {
    long int sz, i;
    PyListObject *list;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    sz = ((PyVarObject *)(p))->ob_size;
    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", sz);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < sz; i++) {
        item = list->ob_item[i];
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
