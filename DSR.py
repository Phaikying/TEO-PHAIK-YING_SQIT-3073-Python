
import os #operating system

def calculate_monthly_instalment(principal, int_rate, year):
    monthly_interest = int_rate / 100 / 12 #decimal monthly interest rate
    n = year * 12 #Number of monthly payment
    monthly_payment = principal * (monthly_interest / (1 - (1 + monthly_interest) ** -n))
    return monthly_payment

n = int(input('Please enter number of years of loan: '))
int_r = float(input('Please enter the annual interest rate: '))
principal = int(input('Please enter the amount of loan: '))

print('Monthly payment: {}'.format(calculate_monthly_instalment( principal, int_r, n)))

def calculate_total_payment(monthly_payment, loan_term_months):
    total_payment = monthly_payment * loan_term_months
    return total_payment

monthly_payment = 1000  # Replace with the actual monthly payment value
loan_term_months = 36  # Replace with the actual loan term in months

print('Total payment: {}'.format(calculate_total_payment(monthly_payment, loan_term_months)))

def calculate_dsr(housing_loan, monthly_income, commitments):
    total_commitments = housing_loan + commitments
    dsr = (total_commitments / monthly_income) * 100
    return dsr

housing_loan = 1000
monthly_income = 5000
commitments = 200

dsr = calculate_dsr(housing_loan, monthly_income, commitments)

if dsr <= 70:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"

print("Debt Service Ratio (DSR): {}%".format(dsr))
print("Eligibility: {}".format(eligibility))

def display_previous_calculations(loan_calculations):
    print("\nPrevious Loan Calculations:")
    
    for i, record in enumerate(loan_calculations, start=1):
        print(f"{i}. principal: RM {round(record.principal, 2)},")
        print(f"   Monthly instalment: RM {round(record.monthly_payment, 2)},")
        print(f"   Total Amount Payable: RM {round(record.total_amount, 2)},")
        print(f"   DSR: {round(record.dsr, 2)}%,")
        print(f"   Eligibility: {record.eligibility}")
        print()
    
    input("Press Enter to continue....")

def edit_record(loan_calculations):
    while True:
        try:
           print("\nPrevious Loan Calculations:")
           i=1
           for record in loan_calculations:
               
               print(str(i) + ". Principal: RM " + str(round(record.principal,2)) 
               + ",\n   Monthly Instalment: RM " + str(round(record.monthly_payment,2))
               + ",\n   Total Amount Payable: RM " + str(round(record.total_amount,2))
               + ",\n   DSR: " + str(round(record.dsr,2)) + "%" 
               + ",\n   Eligibility :" + str(record.eligibility))
               print()
               i+=1

           print()
           
                    
           a=int(input("\nwhich one you want to delete :"))
           del loan_calculations[a-1]
           print("deleted!")
           print() 
           input("Press Enter to continue....")
           break
        except:
            print("Please insert again....")
            input()
            os.system("cls")

class LoanRecord:
    def __init__(self, principal, monthly_payment, total_amount, dsr, eligibility):
        self.principal = principal
        self.monthly_payment = monthly_payment
        self.total_amount = total_amount
        self.dsr = dsr
        self.eligibility = eligibility

