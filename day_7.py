def main(arr, n):
	if len(arr) == n:
		arr.reverse()
		str1 = ' '.join(str(e) for e in arr)
		return str1
	
if __name__ == '__main__':	
	n = int(input().strip())
	arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	# print(main(arr, n))
	print(main(arr, n))



