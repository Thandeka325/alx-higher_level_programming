#include "lists.h"
#include <stdlib.h>
#include <stdlib.h>

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to pointer of the first node
 * Return: Pointer to the new head of the reversed list
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
	*head =  prev;

	return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to pointer of the first node
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half = NULL,
		  *first_half = *head;

	/* Step 1: Find the middle of the list */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	/* Step 2: Reverse the second half */
	second_half = slow;
	reverse_list(&second_half);

	/* Step 3: Compare the two halves */
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			reverse_list(&second_half);
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	/* Restore the original list */
	reverse_list(&second_half);
	return (1);
}
