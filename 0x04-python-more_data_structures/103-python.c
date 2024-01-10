#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about Python list objects.
 * @p: A PyObject pointer representing the Python list to be printed.
 */
void print_python_list(PyObject *p)
{
	unsigned long int size, allocated;
	PyObject *item; /* item: current list item */
	PyListObject *list; /* list: casted PyObject to PyListObject */

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", allocated);

	for (unsigned int i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %u: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about Python byte objects.
 * @p: A PyObject pointer representing the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes; /* bytes: casted PyObject to PyBytesObject */
	unsigned long int size; /* size: size of the byte object */
	char *str; /* str: string representation of the byte object */

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);
	str = bytes->ob_sval;

	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes:", size < 10 ? size + 1 : 10);

	for (unsigned int i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", str[i] & 0xff);
	}
	printf("\n");
}
