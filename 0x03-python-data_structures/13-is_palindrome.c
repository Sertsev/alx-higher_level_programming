#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* is_palindrome - checks if list is palindrome
* @head: list
*
* Return: 1 if palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	int i;
	int j;
	int k;
	listint_t *mypointer;
	int myarray[10000];

	i = j = 0;
	if (head == NULL || *head == NULL)
	return (1);
	mypointer = *head;
	if (mypointer->next == NULL)
	return (1);
	
	while (mypointer)
	{
		myarray[j] = mypointer->n;
		mypointer = mypointer->next;
		j++;
	}
	j--;
	k = j / 2;
	while (i < k)
	{
		if (myarray[i] == myarray[j])
		{
			i++;
			j--;
		}
		else
		return (0);
	}
	return (1);
}
