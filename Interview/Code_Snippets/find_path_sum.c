void findPathSum(Tree *root, path *patharr, int sum, int level)
{
	if(root == NULL)
		return NULL;
	
	path[level] = root->data;
	int s = 0;
	
	for(int i = level; i > 0; i--)
	{
		s = s + path[i];
		if(s == sum)
		{
			printPath(path, i, level);
		}	
	}
	
	findPathSum(root->left, patharr, sum, level+1);
	findPathSum(root->right, patharr, sum, level+1);
	
	path[level] == NULL; //remove the data as it didnt 
		
}

void findPath(Tree *root, int sum)
{
	int *patharr;
	int height = findTreeHeight(root);
	findPathSum(root, patharr, sum, 0)
}

void printPath(int *patharr, int start, int end)
{
	for(int i = start; i <= end; i++)
	{
		print(path[i]);
	}
}