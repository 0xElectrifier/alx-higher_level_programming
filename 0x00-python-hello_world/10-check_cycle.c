#include "lists.h"

/**
 * check_cycle - function that checks if a listint_t list contains a cycle
 * @list: pointer to ilst to be checked
 *
 * Description: algorithm was solved using the Floyd's cycle finding algorithm
 * Return: 0 on success
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
