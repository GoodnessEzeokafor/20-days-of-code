


def main(n,new_dict):
	message = "Not Found"
	new_list = []
	for i in range(n):
		testcase = input()
		new_list.append(testcase)

	for i in new_list:
		if i in new_dict:
			message = i+" = "+new_dict[i]
		else:
			message = "Not Found"
		print(message)


if __name__ == '__main__':
	n = int(input())
	new_dict = {}
	for i in range(0,n):
		keys = input().split(" ")
		new_dict[keys[0]] = keys[1]
	main(n,new_dict)




