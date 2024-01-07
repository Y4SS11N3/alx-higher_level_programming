#include "lists.h"

/**
 * reverse_list - reverses a singly linked list
 * @head: double pointer to the start of the linked list
 *
 * Return: pointer to the start of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - determines if the elements of a singly linked list
 *                 can be read the same forwards and backwards
 * @head: double pointer to the start of the linked list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = *head;
	listint_t *second_half, *middle = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;
		reverse_list(&second_half);

		res = compare_lists(*head, second_half);

		reverse_list(&second_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = second_half;
		}
		else
			prev_slow->next = second_half;
	}
	return (res);
}

/**
 * compare_lists - compares two singly linked lists
 * @head1: pointer to the start of the first list
 * @head2: pointer to the start of the second list
 *
 * Return: 1 if the lists are the same, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}
