#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
#define PY_SSIZE_T_CLEAN

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: A Python object, assumed to be a list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	Py_ssize_t size;
	Py_ssize_t allocated;
	PyObject *item;
	PyListObject *list = (PyListObject *)p;

	/* Check if the object is a list */
	if (!PyList_Check(p))
	{
		fprint(stderr, "Invalid List Object\n");
		return;
	}
	/* Get the size of the list */
	size = PyList_Size(p);
	allocated = list->allocated;

	printf("[*] Size of Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	/* Print the type of each element */
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
