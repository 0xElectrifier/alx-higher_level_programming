#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <string.h>

/**
 * print_python_bytes - prints basic info  about Python bytes
 * @p: Python bytes passed from .py file
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, lim, i;

	printf("[.] bytes object info\n");
	if(!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = PyBytes_AsString(p);
	size = ((PyVarObject *)(p))->ob_size;
	if (size > 10)
		lim = 10;
	else
		lim = size + 1;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", lim);
	for (i = 0; i < lim; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	}
	printf("\n");
}

/**
 * print_python_list - prints basic info about Python lists
 * @p: Python list
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	if (!PyList_Check(p))
		return;

	list = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		obj = list->ob_item[i];
		printf("Element %ld: %s\n", i, (obj->ob_type)->tp_name);
		if (PyBytes_Check(obj->ob_item[i]))
			print_python_bytes(obj);
	}
}
