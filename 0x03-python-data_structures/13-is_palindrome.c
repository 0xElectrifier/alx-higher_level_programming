#include "lists.h"

/**
 * is_palindrome - Function in C that checks if a singly linked list
 * 		is a palindrome
 * @head: pointer to to pointer to head of list
 * Return: 0 if list is not palindrome otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr, *slow_ptr;
	listint_t *firstHalf_ptr, *secondHalf_ptr;

	if (!head || !*head)
		return (1);
	fast_ptr = slow_ptr = firstHalf_ptr = *head;
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr != NULL)
		secondHalf_ptr = slow_ptr->next->next;
	else
		secondHalf_ptr = slow_ptr->next;
	while (firstHalf_ptr && secondHalf_ptr)
	{
		if (firstHalf_ptr->n != secondHalf_ptr->n)
			break;
		firstHalf_ptr = firstHalf_ptr->next;
		secondHalf_ptr = secondHalf_ptr->next;
	}
	if (secondHalf_ptr != NULL)
		return (0);

	return (1);
}
