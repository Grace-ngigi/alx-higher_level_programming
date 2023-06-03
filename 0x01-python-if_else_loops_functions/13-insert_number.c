#include "lists.h"
#include <stdlib.h>

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
