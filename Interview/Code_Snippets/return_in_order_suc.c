Tree * returnInOrderSuc(Tree * root)
{
	if(root == NULL)
		return NULL;
	
	if(root->right != NULL)
		return leftMostOfRightSubTree(root);
	
	Tree *x = root;
	Tree *p = root->parent;
	
	while(p != NULL && p->left != x)
	{
		x = p;
		p = p->parent;
	}
	
	return p;
}

Tree * leftMostOfRightSubTree(Tree *root)
{
	if(root == NULL)
		return NULL;
	
	while(root->left != NULL)
	{
		root = root->left;
	}
	
	return root;
}