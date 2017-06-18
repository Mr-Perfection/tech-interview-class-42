'''
Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one 
character. Find all possible words that can be formed by a sequence of adjacent characters. 
Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of 
same cell.

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = [[]]'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};

Output:  Following words of dictionary are present
         GEEKS
         QUIZ

Amazon

I assumed that strings are not empty inside dictionary
i = 0, word = GEEKS
G->E->E->K->S Check top, right, left, right and keep track of visited letters.
print 
'''

def is_boggle(word, visited, boggle, row, col):
    # base case: if word is empty
    if not word:
        return True
    # base case: if visited[row][col] is True, return False
    if visited[row][col]:
        return False
    
    visited[row][col] = True
    result = False
    # if the letter matches with element from boggle
    # explore top, top right, top left, left... possible ways.
    if word[0] == boggle[row][col]:
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if 0 <= i < len(boggle) and 0 <= j < len(boggle[0]):
                    result = is_boggle(word[1:], visited, boggle, i, j) or result
    # uncheck visited so that it allows to explore other possibilities.
    visited[row][col] = False
    return result

    


def Boggle(dictionary: list, boggle: list):
    
    if not(boggle) or not(dictionary):
        return
    
    n,m = len(boggle), len(boggle[0])
    
    # iterate through boggle words
    for word in dictionary:
        visited = [[False for col in range(m)] for row in range(n)]
        for row in range(n):
            for col in range(m):
                if not visited[row][col]:
                    if is_boggle(word, visited, boggle, row, col):
                        print(f"{word} is valid!") # f-string interpolation Python 3.6+
        
                    
dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
boggle = [['G','I','Z'],['U','E','K'],['Q','S','E']]

Boggle(dictionary, boggle)