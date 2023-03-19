credit = float(input("Enter the load principal: \n>"))
task = input("What do you want to calculate?\n\
type 'm'  for number of monthly payments\n\
type 'p' – for the monthly payment:\n\
> ")
if task == "m":
    payment = int(input("Enter the monthly payment\n\
>"))
    monthly_payment = credit // payment
    print("It will take", monthly_payment,"months to repay the loan")
elif task == "p":
    month = int(input("Enter the number of months:\n\
> "))
    monthly_payment = credit // month
    print("Your monthly payment =", monthly_payment)
