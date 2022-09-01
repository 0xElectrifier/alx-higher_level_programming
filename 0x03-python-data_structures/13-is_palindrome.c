#include "lists.h"

/**
 * list_len - checks for the length of a linked list
 * @head: pointer to head of list
 *
 * Return: length of iist
 */
int list_len(listint_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		head = head->next;
		len++;
	}

	return (len);
}

/**
 * is_palindrome - Function in C that checks if a singly linked list
 * 		is a palindrome
 * @head: pointer to to pointer to head of list
 * Return: 0 if list is not palindrome otherwise 1
 */
int is_palindrome(listint_t **head)
{
	int len, i, j, back_idx;
	listint_t *list_fwd, *list_bck;

	if (!head || !*head)
		return (1);

	list_fwd = *head;
	len = list_len(*head);
	back_idx = len;
	i = 0;

	while (list_fwd && (i < len / 2))
	{
		list_bck = *head;
		j = 0;
		while (list_bck && (j < back_idx - 1))
		{
			list_bck = list_bck->next;
			j++;
		}
		if (list_bck && (list_fwd->n != list_bck->n))
			break;
		list_fwd = list_fwd->next;
		back_idx--;
		i++;
	}
	if (i != len / 2)
		return (0);

	return (1);
}
