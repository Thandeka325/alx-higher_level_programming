#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A Pyobject list.
 */
void print_python_lists(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: A PyObject bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(P))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyByte Size(p);
	string = PyBytes_AsString(p);

	printf(" size: %zd\n", size);
	printf(" trying string: %s\n", string);
	printf(" first %zd bytes: ", size < 10 ? size + 1 : 10);

	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%02hhx", string[i]);
		if (i < size && i != 9)
			printf(" ");
	}
	printf("\n");
}
