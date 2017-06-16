'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

add 1, 3, 5, 10, 9
[1, 5, 9, 10, 3]
total += ... = 1 + 3 + 5 + 10 + 9 = 28
find(4)
    { 1 } also check if 3 exists inside set
    { 5 } also checks if -1 exists ...
    { 9 } also checks ...
    { 10 } also checks ...
    { 3 } also checks if 1 is inside set! congrats, you find it!
    return true
    

Linkedin
'''

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
        check = set()
        arr = self.arr

        # if array is empty, not found
        if not arr:
            return False
        for number in arr:
            if value - number in check:
                return True # found it.
            check.add(number)

        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
