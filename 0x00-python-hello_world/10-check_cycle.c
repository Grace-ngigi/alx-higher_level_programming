#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks for a cycle in a linked list
 * @list: pointer to a struct
 * Return: 1 if cycle else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (first != NULL && second != NULL && second->next != NULL)
	{
		/* one step */
		first = first->next;
		/* two steps */
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
