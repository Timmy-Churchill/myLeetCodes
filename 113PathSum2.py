# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def pathSum(self, root:list, targetSum: int) -> list: #list of lists
        
        depth = math.log(len(root) + 1, 2)

        numPaths = (len(root) + 1)/2

        possiblePaths = []
        for i in range(numPaths):
            possiblePaths.append('.')

        for i in range(depth):
            for index, path in enumerate(possiblePaths.copy()):
                pathCopy = path.copy()
                path.append(index*2 + 1)
                pathCopy.append(index*2)
                possiblePaths[index] = path
                possiblePaths.append(pathCopy())
            

        
            

        #have a multiplier by 2 to figure out the baby nodes of each one
        #generate all nodes - first figure out the length by adding one then logging it

        #start with the top
        #repeat depth times: baby indexes = i*2, i*2 + 1.


