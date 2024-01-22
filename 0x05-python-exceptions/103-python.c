#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Prints data of a Python float object.
 * @p: PyObject pointer.
 */
void print_python_float(PyObject *p)
{
	double val = 0;   /* Float value */
	char *str = NULL; /* String representation of float */

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - Prints data of a Python bytes object.
 * @p: PyObject pointer.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0; /* Size of bytes object */
	Py_ssize_t i = 0;    /* Loop index */
	char *str = NULL;    /* String representation of bytes */

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", str[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - Prints data of a Python list object.
 * @p: PyObject pointer.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0; /* Size of list */
	PyObject *item;      /* List item */
	int i = 0;           /* Loop index */

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

