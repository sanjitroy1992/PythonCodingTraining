"""
Steps:
- run a outer loop i which will iterate every value in the string.
- run a inner loop j which will check only the substring and if any character doesn't match in the string it brakes.
"""

def CountOccurrences(string, substring):
	n = len(string)
	m = len(substring)
	for i in range(n-m+1):
		flag = 0
		for j in range(m):
			if string[i+j] != string[j]:
				flag = 1
				break
		if flag == 0:
			print(i)

string = "GeeksforGeeksforGeeksforGeeks"
print(CountOccurrences(string, "GeeksforGeeks"))
