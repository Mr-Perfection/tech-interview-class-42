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

FB
'''

'''
[1] // root
[1, 2] // left
[1, 2, 5] // left is None but right is 5
[1, 2, 5] // left is None and right is None. Add this into Solution list.
[1, 2] // recurse back...
[1]
[1, 3] // lets go right
[1, 3] // left and right are None. So, add it to Solution list.
'''

def helper(root, candidate, solution):
  # base case #1: if left and right are None, add cand. to solution
  if not(root.left) and not(root.right):
    solution.append(candidate)
    return
  
  if not(root.left):
    helper(root.left, candidate + '->' + str(root.left.val), solution)
  
  if not(root.right):
    helper(root.right, candidate + '->' + str(root.right.val), solution)


def Solution(root):
  
  if not(root): return None

  solution = []
  helper(root, str(root.val), solution)
  return solution

  '''
  Time: O(n), Space: O(n) 
  test #1:
          5
       4    10
     3   1     19
  
  Solution(root)
  5->, []
  5->4, []
  5->4->3, [5->4->3]
  5->4, [5->4->3]
  5->4->1, [5->4->3, 5->4->1]
  5->4, [5->4->3, 5->4->1]
  5, [5->4->3, 5->4->1]
  5->10, [5->4->3, 5->4->1]
  5->10->19, [5->4->3, 5->4->1, 5->10->19]
  '''