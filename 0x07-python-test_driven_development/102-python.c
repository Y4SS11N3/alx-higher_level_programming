#include "Python.h"

/**
 * print_python_string - Displays Python string details.
 * @p: Python string object.
 */
void print_python_string(PyObject *p)
{
	long int len; /* Length of the string */

	fflush(stdout);

	printf("[.] string object info\n");
	/* Check if object type is 'str' */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = ((PyASCIIObject *)(p))->length; /* Retrieve string length */

	/* Determine string type: ASCII or Unicode */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", len); /* Print string length */
	/* Print string value */
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}

