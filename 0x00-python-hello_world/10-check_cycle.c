#include "lists.h"

/**
 * check_cycle - function that checks if a listint_t list contains a cycle
 * @list: pointer to ilst to be checked
 *
 * Return: 0 on success
 */
int check_cycle(listint_t *list)
{
	listint_t **list_p, *copy;

	if (list == NULL)
		return (0);

	list_p = &list;
	copy = list->next;
	while (copy != NULL)
	{
		if (*list_p == copy)
			return (1);

		copy = copy->next;
	}

	return (0);
}

