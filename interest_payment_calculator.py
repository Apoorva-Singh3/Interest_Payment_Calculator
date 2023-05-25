def main():
    print('')
    print('This is a Monthly Loan Payment Calculator')
    print('')
    
    principal = float(input('Enter the loan amount : '))
    apr = float(input('Enter annual interest rate : '))
    years = int(input('Enter number of years : '))
    
    monthly_rate = apr / 1200
    total_months = years * 12
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** (-total_months))
    
           
    print('The monthly payment for the loan is : %.2f ' % monthly_payment)
    
main()