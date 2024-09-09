#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: Pointer to the start of the singly linked list
 *
 * Return: 0 if no cycle, 1 if cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (hare != NULL && hare->next != NULL)
	{
		if (tortoise == hare)
			return (1); /* Cycle found */

		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0); /* No cycle */
}
