#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	printf("[*] Size of the Python List = %li\n", PyList_Size(p));
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (int i = 0; i < PyList_Size(p); i++) {
		printf("Element %i: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
