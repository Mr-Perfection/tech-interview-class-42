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
class Node(object):
  val = 0
  left, right = None, None

  def __init__(self, val):
    self.val = val