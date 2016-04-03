def loan():
	# p  : Principal
	# ar : Annual interest rate
	# t  : Total time period (in Years)
	# ppy: Payments or Periods per year

	p	= input("Loan amount  (i.e. Principal)      : ")
	ar	= input("Annual interest rate  (percentage) : ")
	t	= input("Loan period           (years)      : ")
	oneprd	= input("Period of one payment (months)     : ")

	ar	=	ar/100.0
	ppy	=	12.0/oneprd
	pi	=	ar/ppy		# pi: Periodic interest rate
	n	=	t*ppy		# n : Total number of payments

	installment = (p*pi)/(1.0 - (1.0 + pi)**(-n))	# regular withdrawals or size of each installment
	
	amount   = installment * n
	interest = amount - p

	print("\nEach Installment : %15.2lf" % installment)
	print("Total Interest   : %15.2lf" % interest)
	print("Total Amount     : %15.2lf" % amount)


	
	
def invest():
	# p  : Principal
	# ar : Annual interest rate
	# t  : Total time period (in Years)
	# ppy: Payments or Periods per year

	p	= input("Initial investment                  : ")
	ar	= input("Annual return rate  (percentage)    : ")
	t	= input("Investment period   (years)         : ")
	ppy	= input("No. of compounding periods per year : ")

	ar	= ar/100.0
	pi	= ar/ppy	# pi: Periodic interest rate
	n	= t*ppy		# n : Total number of payments

	amtci	= p * ( (1.0 + pi)**n )
	ci	= amtci - p

	amtsi	= p * ( 1.0 + pi*n )
	si	= amtsi - p

	print("\nUsing Compound Interest method,")
	print("Total Compounded Amount : %15.2lf" % amtci)
	print("Compound Interest       : %15.2lf" % ci)

	print("\nUsing Simple Interest method,")
	print("Total Amount            : %15.2lf" % amtsi)
	print("Simple Interest         : %15.2lf" % si)

	
	
	
def annuity():
	# p  : Principal
	# ar : Annual interest rate
	# t  : Total time period (in Years)
	# ppy: Payments or Periods per year

	wd	= input("Desired regular withdrawal        : ")
	ar	= input("Annual return rate  (percentage)  : ")
	t	= input("Time Period         (years)       : ")
	oneprd	= input("Period of each withdrawal (months): ")

	ar	= ar/100.0
	ppy	= 12.0/oneprd
	pi	= ar/ppy	# pi: Periodic interest rate
	n	= t*ppy		# n : Total number of payments

	p	= wd * ( 1.0 - (1.0 + pi)**(-n) )/ pi
	interest= wd*n - p

	print("\nInitial investment required : %15.2lf" % p)
	print("Interest (extra money)      : %15.2lf" % interest)


