def main(n):
	for i in range(1,11):
		print(n, "x", i,"=", n*i)



if __name__ == '__main__':
	n = int(input().strip())
	main(n)