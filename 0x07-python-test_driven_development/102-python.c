#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject pointer representing a Python string object.
 *
 * Description: If the object is not a valid string, prints an error message
 * otherwise, it prints the type, length, and value of the string.
 */
void print_python_string(PyObject *p)
{
	/* Check if the object is a valid Unicode object */
	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n  [ERROR] Invalid String Object\n");
		return;
	}

	/* Fetch the string type: ASCII or Unicode */
	const char *type = PyUnicode_IS_COMPACT_ASCII(p) ?
		"compact ascii" : "compact unicode object";

	/* Get the length and the string value */
	Py_ssize_t length = PyUnicode_GET_LENGTH(p);
	const char *value = PyUnicode_AsUTF8(p);

	/* Print the string information */
	printf("[.] string object info\n");
	printf("  type: %s\n", type);
	printf("  length: %zd\n", length);
	printf("  value: %s\n", value);
}
