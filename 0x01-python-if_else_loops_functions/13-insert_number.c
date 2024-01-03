#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the pointer of the first node of the list
 * @number: The number to insert
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (head == NULL)
		return (NULL);

	/* Create new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	/* Case: insert at beginning or in an empty list */
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		/* Find the correct position to insert */
		current = *head;
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}

		/* Insert new node */
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
