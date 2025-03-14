# Sorted array to BST

# Given a sorted array, convert it into a height balanced BST

# Solution: The middle element of the array will be the root of the BST. The left half of the array will be the left subtree and the right half of the array will be the right subtree. Recursively build the left and right subtrees.

# Time complexity: O(n), where n is the number of elements in the array.

# Space complexity: O(log n), where n is the number of elements in the array. The space complexity is O(log n) because the height of a balanced BST is log n.

# Python code to convert a sorted array into a height balanced BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def sortedArrayToBST(nums):
    if not nums:
        return None
    # Find the middle element of the array
    mid = len(nums) // 2
    # Create a new node with the middle element as the root
    root = TreeNode(nums[mid])
    # Recursively build the left subtree
    root.left = sortedArrayToBST(nums[:mid])
    # Recursively build the right subtree
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

# Helper function to print the inorder traversal of the BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Example
nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
inorder(root)  # Output: -10 -3 0 5 9
