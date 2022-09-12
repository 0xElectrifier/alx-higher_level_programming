#include <>

/**
 * print_python_list - prints basic info about Python lists
 * @p: Python list
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n\
		[*] Size of the Python List = %HH\n\
		[*] Allocated = %HH\n
		")
}

/**
 * print_python_bytes - prints basic info  about Python bytes
 * @p: Python bytes passed from .py file
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	printf("size: %d\n", dd);
	printf("first 6 bytes: %HH\n", dd);
}
