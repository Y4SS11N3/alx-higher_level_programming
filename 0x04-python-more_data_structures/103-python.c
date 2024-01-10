#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject pointer representing a Python list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	const char *type_name;
	ssize_t i, size;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		type_name = item->ob_type->tp_name;
		printf("Element %zu: %s\n", i, type_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject pointer representing the Python byte object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	char *str;
	unsigned long size;
	unsigned int i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = Py_SIZE(p);
	str = bytes->ob_sval;

	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes:", size < 10 ? size + 1 : 10);

	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", str[i] & 0xff);
	}
	printf("\n");
}
