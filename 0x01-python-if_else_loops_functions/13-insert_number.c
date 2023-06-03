#include "lists.h"
#include <stdlib.h>

listint_t *sort_list(listint_t **head);

/**
 * insert_node - inserts a node in a sorted list
 * @head: pointer to the head
 * @number: value to be inserted
 * Return: pointer to the created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *trvs, *prev;

	if (*head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL)
	{
		*head = newnode;
		return (newnode);
	}
	trvs = *head;
	prev = NULL;

	while (trvs != NULL && trvs->n < number)
	{
		prev = trvs;
		trvs = trvs->next;
	}
	if (prev == NULL)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		prev->next = newnode;
		newnode->next = trvs;
	}
	sort_list(head);
	return (newnode);
}
/**
 * sort_list - sorts a given list
 * @head: pointer to the given list;s head
 * Return: pointer to the head of the sorted list
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
	return (*head);
}
