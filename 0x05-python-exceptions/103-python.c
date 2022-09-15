#include <Python.h>

/**
 * print_python_float - takes python float and attempts to print it
 * @p: float argument passed from .py function call
 *
 * Return: nothing
 */
void print_python_float(PyObject *p)
{
	double num;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	num = ((PyFloatObject *)(p))->ob_fval;
	str = PyOs_double_to_string(num, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - takes python bytes data and attempts to print it
 * @p: PyObject* passed from .py function call
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	long int i, size, lim;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	size = PyBytes_Size(p);
	lim = size;
	if (size > 10)
		lim = 10;
	else
		lim += 1;

	str = ((PyBytesObject *)(p))->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", lim);
	for (i = 0; i < lim; i++)
	{
		if (str[i] < 0)
			printf(" %02x", str[i] + 256);
		else
			printf(" %02x", str[i]);
	}
	printf("\n");
}

/**
 * print_python_list - prints a python ilst
 * @p: Python ilst passed in .py function to be printed
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int len, alloc, i;
	PyObject *obj;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = ((PyListObject *)(p));
	len = ((PyVarObject *)(p))->ob_size;
	alloc = list->allocated;
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < len; i++)
	{
		obj = list->ob_item[i];
		printf("Element %ld: %s\n", i, (obj->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}
}
