def main(date_returned, date_exp_returned):
	'''
		'
	'''
	fine = 0
	if date_returned[0] == date_exp_returned[0] or date_returned[0] < date_exp_returned[0]:
		fine = 0
	if date_returned[0] > date_exp_returned[0] and date_returned[1] == date_exp_returned[1] and date_returned[2] == date_exp_returned[2]:
		fine = 15 * (date_returned[0] - date_exp_returned[0]) 
	
	if date_returned[1] > date_exp_returned[1] and date_returned[0] == date_exp_returned[0] and date_returned[2] == date_exp_returned[2] :
		fine = 500 * (date_returned[1] - date_exp_returned[1])
	
	if date_returned[2] > date_exp_returned[2]:
		fine = 1000

	print(fine)

if __name__ == '__main__':
	returned = input().split(" ")
	exp_ret = input().split(" ")

	date_returned = [int(i) for i in returned]
	date_exp_returned = [int(i) for i in exp_ret]


	main(date_returned, date_exp_returned)