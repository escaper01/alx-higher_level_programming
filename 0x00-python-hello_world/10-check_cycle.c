#include <stdio.h>
#include "lists.h"
/**
* check_cycle - checks if a singly linked list is cycled
* @list: singly linked list.
* Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if (list == NULL)
		return (0);

	head = list;
	tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);

	}
	return (0);
}
#include <stdio.h>
#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle within.
* @list: singly linked list.
* Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if (list == NULL)
		return (0);

	head = list;
	tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);

	}
	return (0);
}
