#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list;
	PyObject *item;

	if (!PyList_Check(p))
		return;
	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}