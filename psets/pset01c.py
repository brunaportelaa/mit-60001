annual_salary = float(input('Enter the starting salary: '))
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = total_cost * 0.25
number_months = 36
r = .04

def calculate_savings(savings_rate):
    current_savings = 0.0
    monthly_salary = annual_salary / 12

    for month in range(1, number_months + 1):
        portion_saved = monthly_salary * (savings_rate/10000)
        current_savings += portion_saved
        current_savings += current_savings * (r / 12)

        if month % 6 == 0:
            monthly_salary *= 1 + semi_annual_raise

    return current_savings

high = 10000
low = 0
x = (high - low)/2
test = calculate_savings(x)
steps = 0

while abs(test - portion_down_payment) > 100:
    if test > portion_down_payment:
        high = x
    else:
         low = x
    x = (high + low) // 2
    test = calculate_savings(x)
    steps += 1

    if x > 9990:
        break

if x > 9990:
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate: ', x/10000)
    print('Steps in bisection search: ', steps)