bool isSubTree(Tree *root, Tree *rootSub)
{
	if(root == NULL)
		return false;
	
	if(rootSub == NULL)
		return true;
	
	if(root->data == rootSub->data)
		if (matchTree(root, rootSub) == true)
			return true;
	else
		return isSubTree((root->left, rootSub) || isSubTree(root->right, rootSub)
}

bool matchRoot(Tree *root1, Tree *root2)
{
	if (root1 == NULL && root2 == NULL)
		return true;
	
	else (root1 == NULL || root2 == NULL)
		return false
		
	if(root1->data != root2->data)
		return false;
	
	else 
		return (matchRoot(root1->left, root->left) && matchRoot(root1->right, root2->left))
}