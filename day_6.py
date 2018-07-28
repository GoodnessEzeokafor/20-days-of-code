'''
Given a string,S , of length N that is indexed from 0 to N - 1 , print its even-indexed and odd-indexed characters as 
2 space-separated strings on a single line.
'''
T = int(input().strip())

for i in range(0, T):
	S = input()
	even, odd = S[::2], S[1::2]
	print(even + " " + odd)