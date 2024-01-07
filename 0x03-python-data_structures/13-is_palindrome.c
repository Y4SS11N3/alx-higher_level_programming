#include "lists.h"

/**
 * is_palindrome - determines if the elements of a singly linked list
 *                 can be read the same forwards and backwards
 * @head: double pointer to the start of the linked list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *stack = NULL, *temp;
	int is_pal = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = malloc(sizeof(listint_t));
		if (!temp)
			return (0);
		temp->n = slow->n;
		temp->next = stack;
		stack = temp;
		slow = slow->next;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (slow->n != stack->n)
			is_pal = 0;
		slow = slow->next;
		temp = stack;
		stack = stack->next;
		free(temp);
	}

	while (stack)
	{
		temp = stack;
		stack = stack->next;
		free(temp);
	}

	return (is_pal);
}
