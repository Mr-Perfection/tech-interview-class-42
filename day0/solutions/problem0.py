'''
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.

Time Complexity O(n)
Space           O(1)
'''

def FizzBuzz(n):
    for i in range(1, n+1):
        s = ''

        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        if s:
            print(s)
        else:
            print(i)

FizzBuzz(100)
