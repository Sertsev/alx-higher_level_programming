#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdlib.h>
#include <stdio.h>
#define  int Py_ssize_t
/**
 * print_python_list_info - a function prints python list informations
 * @p: pointer to Python Object reference
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
int i, j, k;
PyListObject *list_item;

list_item = (PyListObject *)p;
i = PyList_Size(p);
j = list_item->allocated;
printf("[*] Size of the Python List = %ld\n", i);
printf("[*] Allocated = %ld\n", j);
for (k = 0; k < i; k++)
{
printf("Element %ld: %s\n", k, Py_TYPE(list_item->ob_item[k])->tp_name);
}
}
