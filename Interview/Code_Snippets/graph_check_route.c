typedef enum {Unvisited, Visiting, Visted} State;

bool checkRoute(Graph *g, Node *start, Node *end)
{
	
	//create a queue
	Queue *q;

	for(i=0; i<len(g);i++)
		g[i]->state = State.Unvisited;

	start->state = State.Visiting;
	q->add(start);
	Node *u;

	while(!q->isEmpty())
	{
		u = q->dequeue();
		if(u != NULL)
		{
			Node *adjNodes[] = getAdjNodes(g,u);
			for(i = 0; noOfAdjNodes(g,u); i++)
			{
				if(end == adjNodes[i])
					return true;
				else
					adjNodes[i]->state = State.Visiting;
					q->add(adjNodes[i])
			}
		}
		u->state = State.Visted;
	}
	
	return false;

}