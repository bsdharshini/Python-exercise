'''
Reverse array

For a given array reverse order of its elements.

Input
The first line of input contains integer t,the number of test cases.
In the next t lines t test cases follow.
Each test case cosists of numbers separated by spaces.
In each line, the first number ni is the length of an array.
Next ni numbers are values of the array.

Output
For each test case print elements of the array in reversed order.
Numbers should be separated by single space and answers for each
test case should appear in a separate line.

Example
Input:
2
7 1 2 3 4 5 6 7
3 3 2 11

Output:
7 6 5 4 3 2 1
11 2 3

'''

n=int(input())
for i in range(0,n):
    string =input()
    word=string.split(" ")
    del word[0]
    word.reverse()
    print(" ".join(word))
