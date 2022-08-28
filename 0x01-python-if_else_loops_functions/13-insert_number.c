#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that inserts a number into a sorted singly
 * linked list
 * @head: pointer of pointer to head of list
 * @number: number to be inserted
 *
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copy, *new;

	copy = *head;
	while (copy != NULL)
	{
		if (number > copy->n)
			if (copy->next == NULL || number < (copy->next)->n)
				break;
		copy = copy->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = copy->next;
	copy->next = new;

	return (new);
}
