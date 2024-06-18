#01. Ask for user input:
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

#02. Set necessary global variables
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
number_months = 0

#Getting savings for first year
def update_savings(current_savings, annual_salary, portion_saved, r):
    monthly_savings = (annual_salary * portion_saved)/12
    current_savings += current_savings * r / 12
    current_savings += monthly_savings
    return current_savings

while current_savings < portion_down_payment:
    current_savings = update_savings(current_savings, annual_salary, portion_saved, r)
    number_months += 1
    if number_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

#output the result
print(f'Number of months: {number_months}')


