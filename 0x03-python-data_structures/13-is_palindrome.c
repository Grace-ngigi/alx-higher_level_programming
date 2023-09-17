#include"lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if true, 0 if false
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *current, *next, *prev, *first, *second;

	if (!*head || (*head)->next == NULL)
		return (1);

	/* find the middle */
	slow = fast = *head;
	while (slow != NULL && fast != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* reverse the second half */
	current = slow;
	next = prev = NULL;
	while (current != NULL)
	{
		next = current->next;
		/* reverse the link */
		current->next = prev;
		prev = current;
		current = next;
	}

	/* Compare the two halves */
	/**head = prev;*/
	first = *head;
	second = prev;
	while (first != NULL && second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}
