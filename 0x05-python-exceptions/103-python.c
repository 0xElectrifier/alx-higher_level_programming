#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - takes python float and attempts to print it
 * @p: float argument passed from .py function call
 *
 * Return: nothing
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f\n", ((PyFloatObject *)(p))->ob_fval);
}

/**
 * print_python_bytes - takes python bytes data and attempts to print it
 * @p: PyObject* passed from .py function call
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	long int i, len, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	len = PyBytes_Size(p);
	lim = len;
	if (len > 10)
		lim = 10;

	obj = PyUnicode_FromEncodedObject(p, "utf-8", "strict");
	str = ((PyBytesObject *)(obj))->ob_sval;
	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:");
	for (i = 0; i < lim; i++)
	{
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

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	list = ((PyListObject *)(p));
	len = p->ob_size;
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
