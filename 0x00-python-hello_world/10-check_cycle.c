#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks the singly linked list
 * @list: head of linked list
 *
 * Return: 1 for cycle 0 cycle lacks
 */

int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	if (!list)
		return (0);
	/*transversethrough node of existing linked list*/
	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;

		if (s == f) /*cycle found for matching nodes*/
			return (1);
	}
	return (0);
}
