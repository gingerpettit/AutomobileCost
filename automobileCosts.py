#This program asks the user for monthly costs for their automobile expenses
#then display the total monthly cost of these expenses.

#Define the global variable.
MONTHS=12

def main():
    #Get the user to unput the cost for each expense.
    loanPayment = float(input("Enter the monthly cost for your loan payment: "))
    insurance = float(input("Enter the monthly cost for your insurance: "))
    gas = float(input("Enter the monthly cost for your gas: "))
    oil = float(input("Enter the monthly cost for your oil: "))
    tires = float(input("Enter the monthly cost for your tires: "))
    maintenance = float(input("Enter the monthly cost for your maintenance: "))

    #Call the function calculate_months_expenses to get the totalMonthsExpenses
    totalMonthlyCost=calculate_months_expenses(loanPayment,insurance,gas,oil,tires,maintenance)

    #Display the total expenses per month.
    print("The total cost per month for these expenses is $",format(totalMonthlyCost,",.2f"),)

    #Call the function yearly_expenses to calculate the annual expense.
    totalAnnualCost=yearly_expenses(totalMonthlyCost)

    #Print the annual expense.
    print("The total annual cost for these expenses is $", format(totalAnnualCost, ",.2f"), )

#This section is calculating the months expenses.
def calculate_months_expenses(num1,num2,num3,num4,num5,num6):
    calculateMonthsExpenses=num1+num2+num3+num4+num5+num6
    return calculateMonthsExpenses

#This section is calculating the annual expenses.
def yearly_expenses(num1):
    yearsExpenses=num1*MONTHS
    return yearsExpenses

main()
