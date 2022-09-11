
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - CPython function that prints some basic info about
 *                              Python lists
 * @p:
 * Return:
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *obj;
	int list_len, i;
	int alloc;

	if (!PyList_Check(p))
		return;

	bj = (PyListObject *)p;
	list_len = PyList_Size(p);
	alloc = (int)obj->allocated;

	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < list_len; i++)
	{
		printf("Element %d: %s\n", i, (PyList_GetItem(p, i)->ob_type)->tp_name);
	}
}

