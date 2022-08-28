#include "lists.h"
#include <stdlib.h>

/**
 * not_null - function that checks if list or list->n is null
 * @head: pointer to list
 *
 * Return: 1 if true otherwise, 0
 */
int not_null(listint_t *head)
{
	return (head && head->n);
}
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

	if (head == NULL)
		return (NULL);

	copy = *head;
	while ((copy) && (number >= copy->n))
	{
		if (copy->next == NULL || number < (copy->next)->n)
			break;
		copy = copy->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if ((*head == NULL) || (number < (*head)->n))
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		new->next = copy->next;
		copy->next = new;
	}

	return (new);
}
