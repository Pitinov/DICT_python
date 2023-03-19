from tasks import BrainOfCalc


class CreditCalc:
    task = ''
    while task != 'ex':
        task = input("What do you want to calculate?\n\
type 'n' for number of monthly payments,\n\
type 'a' for annuity monthly payment amount,:\n\
type 'p' for loan principal:\n\
type 'ex' to exit\n\
> ")


if task == 'n':
    BrainOfCalc.n_type()
elif task == 'a':
    BrainOfCalc.a_type()
elif task == 'p':
    BrainOfCalc.p_type()
elif task == 'ex':
    print("good bye!")
    break
