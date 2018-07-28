'''
Task 
Given N names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. 
For each names queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
 if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

INPUT FORMAT

The first line contains an integer, n, denoting the number of entries in the phone book. 
Each of the n subsequent lines describes an entry in the form of  2space-separated values on a single line. 
The first value is a friend's name, and the second value is an 8-digit phone number.

After the n lines of phone book entries, there are an unknown number of lines of queries. 
Each line (query) contains a  name to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.


'''

def main(n, key, value):
	d = dict()
	d[key] = value;
	if len(d) == n:
		for key, val in d.items():
			print(key,'=',val)
	if key not in d.keys():
		print('Not found')


if __name__ == '__main__':
	n = int(input().strip())
	for i in range(0,n):
		key,value = input("").split()
	main(n, key, value)
