'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

base case:
  whenever the node doesn't have left or right nodes, then thats the path.
  check left node before traversal
  check right node before traversal
FB
'''
class Node(object):
  val = 0
  left, right = None, None

  def __init__(self, val):
    self.val = val

def helper(root, path, sol):
  # base case
  if not root.left and not root.right:
    sol.append(path + str(root))
    return
  
  # check if right node exists
  # traverse to right sub-tree.
  if root.right:
    helper(root.right, path + str(root.val) + '->', sol)
  
  # check if left node exists
  # traverse to left sub-tree.
  if root.left:
    helper(root.left, path + str(root.val) + '->', sol)
  
  
'''
                        5
            4                  10
        2       8           3     15

helper(5, '', [])
helper(10, '5->', [])
helper(15, '5->10->', [])
sol = [5->10->15]
helper(3, '5->10->3', [5->10->15])
sol = [5->10->15, 5->10->3]
helper(4, '5->', [5->10->15, 5->10->3])
helper(8, '5->4->', [5->10->15, 5->10->3])
sol = [5->10->15, 5->10->3, 5->4->8]
helper(2, '5->4->', [5->10->15, 5->10->3, 5->4->8])
sol = [5->10->15, 5->10->3, 5->4->8, 5->4->2]
'''

def Solution(root):
  # if root is null
  if not root:
    return None

  sol = []
  helper(root, '', sol)

  return sol