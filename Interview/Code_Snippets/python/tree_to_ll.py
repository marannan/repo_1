#convert binary tree to doubly linked list

#algorithm
#*********
#BiNode convert(root)
   #left = convert(root.left)
   #right = convert(root.right)
   #merge_ll(left, root, right)
   #return left
   

#convert to circular ll because its easy to get the tail for left part 
#else it'll take another O(n) to get the tail for each split making the solution O(n^2)
#or you can use a data struct to hold head and tail so merging of left and right parts are done easily with O(n) time

#using circular ll
def convert(root):
   if root == None:
      return None
   
   left_part = convert(root.left)
   right_part = convert(root.right)
   
   if left_part == None and right_part == None:
      return root
   

   if right_part == None:
      tail = None
      
   else:
      tail = right_part.left
      
   
   #join left to root as circular linked list
   if left_part == None:
      join(right_part.left, root)
   
   else:
      join(left_part.left, root)
      
      
   #join right to root as circular linked list
   if right_part == None:
      join(root, left_part)
   
   else:
      join(root, right_part)  
      
   
   #join right to left
   if left_part != None and right_part != None:
      join(tail, left_part)
      
   if left_part == None:
      return root
   
   else:
      return left_part
   

#break the circular connection
def break_circular(head):
   head.left.right = None
   head.left = None
   
   return head


   
   