#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to pointer of the first node of the list
 * @number: The integer to be inserted
 *
 * Return: The address of new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;
	listint_t *prev = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;

		while (current != NULL && current->n < number)
		{
			prev = current;
			current = current->next;
		}
		prev->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
