

int checkHeight(tree *root)
{
	int leftHeight = 0, rightHeight = 0; 
	if(root == NULL)
	{
		return 0;
	}

	leftHeight = checkHeight(root->left)
	if(leftHeight == -1)
	{
		return -1;
	}

	rightHeight = checkHeight(root->right)
	if(rightHeight == 1)
	{
		return -1;
	}

	if(abs(leftHeight - rightHeight) > 1)
	{
		return -1;
	}

	else
	{
		return (max(leftHeight, rightHeight) + 1)
	}

}






bool isBalanced(Tree *root)
{

	if(checkHeight(root) == -1)
		return falsel;
	else
		return true;
	
}