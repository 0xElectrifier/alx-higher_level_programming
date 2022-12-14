#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - CPython function that prints some basic info about
 *				Python lists
 *
 * @p: list to be passed in a python file
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *obj;
	int list_len, i;

	if (!PyList_Check(p))
		return;

	obj = (PyListObject *)p;
	list_len = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < list_len; i++)
	{
		printf("Element %d: ", i);
		printf("%s\n", ((obj->ob_item[i])->ob_type)->tp_name);
	}
}

