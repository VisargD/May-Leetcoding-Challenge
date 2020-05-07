# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        # Declaring an empty list to store the depth and parent of the node.
        parents_and_depth = []
        
        # Recursive DFS function which will search for the two required nodes.
        def get_depth(node, node_value1, node_value2, depth, parent, parents_and_depth):
            
            # If node is None then exit from this function. This is checked everytime when the dfs is called recursively.
            if node == None:                
                return

            # If the value of node equals to the first required node then append its depth and parent in the list.
            if node.val == node_value1:
                parents_and_depth.append(depth)
                parents_and_depth.append(parent)

            # Else if value of node is equal to the second required node then append its depth and parent in the list.
            elif node.val == node_value2:
                parents_and_depth.append(depth)
                parents_and_depth.append(parent)
            
            # If the value of node does not match any of the two then perform dfs recursively and go to the left node.
            # Everytime depth increases by 1 as we move deeper.
            # If it is still not equal to any of the two, move left until there is no node on the left.
            # If there is node becomes None on left than then move to right.           
            else: 
                                  
                get_depth(node.left, node_value1, node_value2, depth + 1, node, parents_and_depth)
            
                get_depth(node.right, node_value1, node_value2, depth + 1, node, parents_and_depth)

        # Call the get_depth function with the following parameters.
        # Initially start with root as node and as parent. Depth will be 0 for root.
        get_depth(root, x, y, 0, root, parents_and_depth)
        
        # After calling the function, check if the list contains 4 elements (depth and parent each for both nodes x and y)
        # If not, then return False
        if len(parents_and_depth) != 4:
            return False
        
        # Condition for cousin is : Level should be same and parent must be different.
        # Check if Levels are same and parent are different.
        # If yes, then return True.
        if (parents_and_depth[0] == parents_and_depth[2]) and (parents_and_depth[1] != parents_and_depth[3]):
            return True

        # Else, return false if any of the two condition is not satisfied.    
        else:
            return False