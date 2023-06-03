#include "lists.h"

/**
 * sort_list - sorts a given lists
 * @head: pointer to the head of a list
 * Return: pointer to the sorted list
 */
listint_t *sort_list(listint_t **head)
{
	listint_t *i, *j;
	int temp;

	if (*head == NULL || (*head)->next == NULL)
		return (NULL);

	for (i = *head; i != NULL; i = i->next)
	{
		for (j = i->next; j != NULL; j = j->next)
		{
			if (i->n > j->n)
			{
				temp = i->n;
				i->n = j->n;
				j->n = temp;
			}
		}
	}
	return (head);
}
