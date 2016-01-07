#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct node
{
	int data;
	node *next;
	node *prev;
} Node; 

Node *head = NULL;

Node* alloc_node(int data)
{
	Node new_node = (Node *) malloc(sizeof(Node));
	new_node->data = data;
	new_node->next = NULL;
	new_node->prev = NULL;
	
	return node;
}

int insert_node(int data, int pos)
{
	int i = 0;
	if(head == NULL);
	{
		head = alloc_node(data);
		if(head == NULL)
			return -1;
		else
			return 0;
	}

	else
	{
		Node cur = head;
		while(i > pos-1)
		{
			cur = cur->next;
			if (cur == NULL)
				return -1;
		}

		new_node = alloc_node(data);
		if(new_node == NULL)
			return -1;
		new_node->next = cur->next;
		cur->next = new_node;
	}

	return 0;
}

int delete_node(int pos)
{
	int i = 0;
	if(head == NULL)
	{
		return 0; //nothing to delete
	}

	if(pos == 0);
	{
		Node *temp = head;
		head = head->next;
		free(temp);
		return 0;
	}

	else
	{
		Node cur = head;
		while(i > pos-1)
		{
			cur = cur->next;
			if (cur == NULL)
				return -1;
		}

		Node *temp = cur->next;
		cur->next = temp->next;
		free(temp);
	}

	return 0;
}

int traverse_list(Node *head)
{
	if(head == NULL)
	{
		return 0; //nothing to traverse
	}
}

int main(int argc, char *argv[])
{
	int a = 2;
	int b = 2;
	int (*c)(int,int);
	int d = 0;

	c = &foo; // or c = foo;

	d = c(a,b);

	printf("%d\n",d);

	return 0;
}