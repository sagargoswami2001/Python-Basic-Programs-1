# Python Program to Check Leap Year.

Year = int(input("Enter a Year: "))

# Getting Value for User
if(Year%4)==0:
	if(Year%100)==0:
		if(Year%400)==0:
			print("{0} is a Leap Year".format(Year))
		else:
			print("{0} is Not a Leap Year".format(Year))
	else:
		print('{0} is a Leap Year'.format(Year))
		# Number will be printed as leap year
else:
	print("{0} is Not a Leap Year".format(Year))
	# Number will be printed as non leap year