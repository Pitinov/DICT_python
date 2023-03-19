import math


class BrainOfCalc:
    @staticmethod
    def n_type():
        loan_principal = float(input("Enter the loan principal\n\
>"))
        monthly_payment = float(input("Enter the monthly payment\n\
>"))
        loan_interest = float(input("Enter the loan interest\n\
>")) / 1200
        n = math.ceil(math.log(monthly_payment / (monthly_payment - loan_interest *
                                                  loan_principal), 1 + loan_interest))
        years, month = divmod(n, 12)
        if years == 0:
            print("It will take {} month to repay this loan!".format(month))
        elif month == 0:
            print("It will take {} years to repay this loan!".format(years))
        else:
            print("It will take {} years and {} months to repay this loan!".format(years, month))

    @staticmethod
    def a_type():
        loan_principal = float(input("Enter the loan principal\n\
>"))
        num = float(input("Enter the number of periods\n\
>"))
        loan_interest = float(input("Enter the loan interest\n\
>")) / 1200
        annuity_payment = loan_principal * (loan_interest * (1 + loan_interest) ** num) / \
            ((1 + loan_interest) ** num - 1)
        years, months = divmod(num, 12)
        if years == 0:
            print("You need to pay {} per month for {} months".format(round(annuity_payment), years))
        elif months == 0:
            print("You need to pay {} per month for {} years".format(round(annuity_payment), years))
        else:
            print("You need to pay {} per month for {} years and {} \n\
                  months".format(round(annuity_payment), years, months))

    @staticmethod
    def p_type():
        annuity_payment = float(input("Enter the annuity_payment\n\
>"))
        num = float(input("Enter the number of periods\n\
>"))
        loan_interest = float(input("Enter the loan interest\n\
>")) / 1200
        loan_principal = annuity_payment / ((loan_interest * (1 + loan_interest) ** num) /
                                            ((1 + loan_interest) ** num - 1))
        years, months = divmod(num, 12)
        if years == 0:
            print("Your loan principal = {} with {} months to \n\
            repay".format(round(loan_principal), months))
        elif months == 0:
            print("Your loan principal = {} with {} years to \n\
                  repay".format(round(loan_principal), years))
        else:
            print("Your loan principal = {} with {} years and {} months\n\
                  to repay".format(round(loan_principal), years, months))