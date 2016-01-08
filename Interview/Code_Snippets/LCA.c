Tree * LCA(Tree *root, Tree *A, Tree *B)
{
	if(root == NULL)
		return NULL;
	
	if(root == A || root == B)
		return root;
	
	Tree *left = LCA(root->left, A, B);
	Tree *right = LCA(root->right, A, B);

	if(left != NULL && right != NULL)
		return root;
	
	if(left != NULL)
		return left;
	
	else if(right != NULL)
	
	return right;
}