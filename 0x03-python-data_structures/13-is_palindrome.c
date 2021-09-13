#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * reverse_list - a function reverses the second half linked list
 * @h: a double pointer of head
 * Return: return the head pointer
 */

void reverse_list(listint_t **h)
{
listint_t *result = NULL;
listint_t *current = *h;
listint_t *next;

while (current != NULL)
{
next = current->next;
current->next = result;
result = current;
current = next;
}
*h = result;
}

/**
 * is_palindrome - a function checks whether the list is palindrome or not
 * @head: a head pointer
 * Return: return 1 is palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
listint_t *current, *mid_last;

current = mid_last = *head;
if (current == NULL || current->next == NULL)
return (1);
while (1)
{
if (!current->next || !current->next->next)
break;
current = current->next->next;
mid_last = mid_last->next;
}
current = mid_last->next;
reverse_list(&current);
mid_last->next = current;
current = *head;
mid_last = mid_last->next;
while (mid_last != NULL)
{
if (current->n != mid_last->n)
return (0);
current = current->next;
mid_last = mid_last->next;
}
return (1);
}
