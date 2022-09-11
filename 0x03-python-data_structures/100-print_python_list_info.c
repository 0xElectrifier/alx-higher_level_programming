#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - CPython function that prints some basic info about
 *				Python lists
 * @p:
 * Return:
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_len, i;
	char *alloc;

	list_len = PyList_Size(p);
	alloc = p->allocated;
/*
	list_len_str = PyBytes_AsString(list_len);
*/	printf("[*] Size of the Python List = %s\n", PyList_Size(p));
	printf("[*] Allocated = %s\n", d);
	for (i = 0; i < list_len; i++)
	{
		printf("Element %d: %s\n", PyList_GetItem(p, i)->ob_type)
	}
}
