'''
####Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

######Input Format

There are 3 lines of numeric input: 
The first line has a double,mealCost  (the cost of the meal before tax and tip). 
The second line has an integer,tipPercent(the percentage of  being added as tip). 
The third line has an integer, taxPercent(the percentage of  being added as tax).


#####Output Format

Print The total meal cost is totalCost dollars., where totalCost is the rounded integer result of the entire bill (mealCost with added tax and tip).

'''

# mealCost type = double
#tipPercent type = int
#taxPercent type = int

def main(mealCost, tipPercent, taxPercent):
	tip = mealCost * (tipPercent/100)
	tax = mealCost * (taxPercent/100)
	totalCost = mealCost + tip + tax
	return round(totalCost)


if __name__ == '__main__':
	mealCost = float(input().strip())
	tipPercent = int(input().strip())
	taxPercent = int(input().strip())
	print("The total meal cost is %s dollars." % main(mealCost, tipPercent, taxPercent))

	