import database
from datetime import datetime

expenses = database.load_expenses()
def add_expense():
    while True:
        # Name
        expense_name = input('Enter expense name: ').title().strip()
        if expense_name in expenses:
            print(f'Expense - {expense_name}, already exists!')
            continue
        break
        # Amount
    while True:
        try:
            expense_amount = float(input('Enter expense amount: ').strip())
        except ValueError:
            print('Amount must be a number!')
            continue
        if expense_amount < 0:
            print(f'Amount - {expense_amount}, cannot be less than zero!')
            continue
        break
        # Category
    while True:
        expense_category = input('1 - Food\n2 - Transport\n3 - Internet\n4 - Other\nChoose category: ').strip()
        if expense_category == '1':
            selected = 'Food'
        elif  expense_category == '2':
            selected = 'Transport'
        elif  expense_category == '3':
            selected = 'Internet'
        elif  expense_category == '4':
            selected = 'Other'
        else:
            print(f'Option - {expense_category}, is invalid!')
            continue
        # Date
        time = datetime.now().strftime("d-%m-%Y %I:%M:%S:%p")
        expense_time = str(time)

        expenses[expense_name] = {
            'amount' : expense_amount,
            'category' : selected,
            'date' : expense_time
        }

        database.save_expenses(expenses)
        print(f'Expense - {expense_name}, added succefully!')

def view_expenses():
    if not expenses:
        print('No expenses made!')
        return

    for name,details in expenses.items():
            print(f'Name - {name}\nAmount - {details["amount"]}\nCategory: {details["category"]}\nTime Created - {details["date"]}\n')

# def search_expenses():
#     if not expenses:
#         print('No expenses made!')
#         return
#
#     search = input('Enter expense name or category: ').title().strip()
#     if search in expenses[search] or expenses[search]['category']:
#         print(f'Name: {expenses[search]}\n Amount: {expenses[]}')
#     else:
#         return None

def update_expense():
    if not expenses:
        print('No expenses made!')
        return

    update_input = input('Enter expense name: ').title().strip()
    if update_input in expenses:
        choice_input = input('1 - Name\n2 - Amount\n3 - Category\n4 - Exit\nChoose an option: ')
        if choice_input == '1':
            while True:
                new_expense_name = input('Enter new name: ').title().strip()
                if new_expense_name in expenses:
                    print(f'Name - {new_expense_name}, already exists!')
                    continue
                expenses[update_input] = new_expense_name
                database.save_expenses(expenses)
                print('Update successful!')
                break
        elif choice_input == '2':
            while True:
                try:
                    new_expense_amount = float(input('Enter new amount: ').strip())
                except ValueError:
                    print('Amount must be a number!')
                    continue
                if new_expense_amount < 0:
                    print(f'Amount - {new_expense_amount}, is less than zero!')
                    continue
                expenses[update_input]['amount'] = new_expense_amount
                database.save_expenses(expenses)
                print('Update successful!')
                break
        elif choice_input == '3':
            while True:
                new_expense_category = input('1 - Food\n2 - Transport\n3 - Internet\n4 - Other\nChoose category: ').strip()
                if new_expense_category == '1':
                    selected = 'Food'
                elif new_expense_category == '2':
                    selected = 'Transport'
                elif new_expense_category == '3':
                    selected = 'Internet'
                elif new_expense_category == '4':
                    selected = 'Other'
                else:
                    print(f'Option - {new_expense_category}, is invalid!')
                    continue
                expenses[update_input]['category'] = selected
                database.save_expenses(expenses)
                print('Update successful!')
                break
        else:
            print(f'Invalid input - {choice_input}')
    else:
        print(f'Name - {update_input}, cannot be found!')












