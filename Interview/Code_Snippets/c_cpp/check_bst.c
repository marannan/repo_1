
int last_val = NULL;
bool checkBST(Tree *root)
{
	if(root == NULL)
		return false;
	
	if(checkBST(root->left) == false)
		return false;
	
	if(last_val != NULL && root->data <= last_val)
		return false;
	
	last_val = root->val;
	
	if(checkBST(root->right) == false)
		return false;
	
	return true;
}