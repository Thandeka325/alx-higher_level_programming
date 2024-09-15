#include "Python.h"
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints info about a Python list
 * @p: List object
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyListobject *pp;

	pp = (PyListObject *)p

	printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);
	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->ty_name);
	}
}
