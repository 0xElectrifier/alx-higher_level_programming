#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <string.h>

/**
 * print_python_list - prints basic info about Python lists
 * @p: Python list
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int list_size, i;
	PyListObject *obj;

	if (!PyList_Check(p))
		return;

	obj = (PyListObject *)p;
	list_size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < list_size; i++)
	{
		printf("Element %li: ", i);
		printf("%s\n", ((obj->ob_item[i])->ob_type)->tp_name);
	}
}

/**
 * print_python_bytes - prints basic info  about Python bytes
 * @p: Python bytes passed from .py file
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	int str_len, lim, i;

	str = PyBytes_AsString(p);
	str_len = strlen(str);
	lim = str_len;
	if (str_len > 10)
		lim = 10;

	printf("[.] bytes object info\n");
	if(!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("size: %d\n", str_len);
	printf("trying string: %s\n", str);
	printf("first %d bytes: ", lim);
	for (i = 0; i < lim; i++)
	{
		printf("%x", str[i]);
		if (i != (lim - 1))
			printf(" ");
		else
			printf("\n");
	}
}
