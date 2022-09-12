#include <byteobject.h>
#include <string.h>

/**
 * print_python_list - prints basic info about Python lists
 * @p: Python list
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *obj;

	if (!PyList_Check)
		return;

	obj = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %HH\n", obj->ob_size);
	printf("[*] Allocated = %HH\n", obj->allocated);
	for (i = 0; i < list_len; i++)
	{
		printf("Element %d: \n", i);
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
	int str_len, lim;

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
	printf("first 6 bytes: ");
	for (i = 0; i < lim; i++)
	{
		printf("%x");
		if (i != (lim - 1))
			printf(" ");
		else
			printf("\n");
	}
}
