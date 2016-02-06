//returns -1 if tree is unbalanced
int checkHeight(Tree *root)
{
	if(root == NULL)
		return 0;
	
	int leftHeight = checkHeight(root->left)
	if(leftHeight == -1)
	{
		return -1;
	}
	
	int rightHeight = checkHeight(root->right)
	if(rightHeight == -1)
	{
		return -1;
	}
	
	int heightDif = abs(leftHeight - rightHeight);
	if(heightDif > 1)
	{
		return -1;
	}
	
	return (max(leftHeight, rightHeight) + 1)
	
}
