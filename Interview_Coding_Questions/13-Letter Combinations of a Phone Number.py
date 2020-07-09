"""
Letter Combinations of a Phone Number LeetCode coding solution. One of Google's most commonly asked interview questions according to LeetCode.

Coding Interviews Letter Combinations of a Phone Number (LeetCode) question and explanation.

This question is a commonly asked by the following companies: Google, Facebook, Amazon, Microsoft, Uber, JPMorgan, and Morgan Stanley.

Link to problem: https://leetcode.com/problems/letter-...

Problem description: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

from collections import deque


# Function to return a list that contains
# all the generated letter combinations
def letterCombinationsUtil(number, n, table):
    list = []
    q = deque()
    q.append("")

    while len(q) != 0:
        s = q.pop()

        # If complete word is generated
        # push it in the list
        if len(s) == n:
            list.append(s)
        else:

            # Try all possible letters for current digit
            # in number[]
            for letter in table[number[len(s)]]:
                q.append(s + letter)

                # Return the generated list
    return list


# Function that creates the mapping and
# calls letterCombinationsUtil
def letterCombinations(number, n):
    # table[i] stores all characters that
    # corresponds to ith digit in phone
    table = ["", "", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]

    list = letterCombinationsUtil(number, n, table)

    s = ""
    for word in list:
        s += word + " "

    print(s)
    return


# Driver program
number = [2, 3]
n = len(number)

letterCombinations(number, n)