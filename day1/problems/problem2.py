'''
Design and implement a TwoSum class. It should support the following operations: 
add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Linkedin
'''
stephen = TwoSum()

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.arr.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        checks = set()
        n = len(self.arr)

        for i in range(n): # 0...n-1
            el = self.arr[i]
            if value - el in checks:
                # hurray, found a pair
                return True
            checks.add(el)
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)