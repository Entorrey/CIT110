    # A program to enter cost of expenses.
...     # 6/11/2022
...     # CTI-110 P1HW2 - Basic Math
...     # Erica Patterson
...     # Pseudocode 

user_expense = input('Enter expense name:')
print('Name of expense:', user_expense)

user_charge = input('Enter monthly charge:')
print('Bill:', user_expense, '-------', 'Before tax:', user_charge)


quotient = 0.06

monthly_tax = (float(user_charge) * quotient)
print('Monthly Tax:', monthly_tax)

monthly_charge = (float(user_charge) + monthly_tax)
print('Monthly charge:', monthly_charge )


annual_charge = monthly_charge * 12
print('Annual charge:', annual_charge) 
