Tree * createMinBST(int *arr, int start, int end)
{
	if(size(arr) == 0)
	{
		return NULL;
	}
		
	if(end < start)
	{
		return NULL;
	}
	
	int mid = (start + end)/2;
	Tree *root;
	root->data = arr[mid];
	root->left = createMinBST(arr, start, mid-1);
	root->right = createMinBST(arr, mid+1, end);
	
	return root;
}