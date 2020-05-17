"""
Anagram: If two words having same characters are called anagram even though the meaning of the word is different.
"""


def anagram(a, b):
    if not len(a)==len(b):
        return False

    str1 = sorted(a.lower())
    str2 = sorted(b.lower())
    if str1 == str2:
        return True
    else:
        return False

print(anagram("abcde", "aBced"))