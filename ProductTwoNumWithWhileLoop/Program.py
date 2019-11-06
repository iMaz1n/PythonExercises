#
#  Program.php
#  Product two numbers with while loop
#
#  Created by Mazen Hrazi on 07/11/19 (Twitter: @iMaz1n).
#  Copyright © 2019 iZONA. All rights reserved.
#

isWantMore = 'y'
while isWantMore == 'y':
	num1 = int(input("Enter number 1: "))
	num2 = int(input("Enter number 2: "))
	product = num1 * num2
	print("The product of two numbers:",product)
	if product < 50:
		print("The product is less than 50")
	isWantMore = input("if you want calculate another numbers, Enter (y): ").lower()
	if isWantMore == 'y':
		continue
	else:
		break
print("-------------------THANK YOU-------------------")