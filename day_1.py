def calculate_average():
    try:
        a = float(input('a: '))
        b = float(input('b: '))
        return (a + b) / 2
    except ValueError:
        return None

# r = calculate_average()
# if r is None:
#     print('Invalid input!')
# else:
#     print(f"Average: {r}")



def calculate_total(price,quantity):
   try:
       total = float(price) * int(quantity)
       return total
   except (ValueError, TypeError):
       return None

# s = calculate_total(100.3,5)
# if s is None:
#     print('Cannot compute!')
# else:
#     print(f"Total: {s}")

def calculate_discounted_price(price,discount):
    try:
        price = float(price)
        discount = float(discount)

        discount_amount = price * (discount / 100)
        final_price = price - discount_amount
        return  final_price
    except (TypeError, ValueError):
        return None

d = calculate_discounted_price(1000,20)
if d is None:
    print('Cannot compute!')
else:
    print(f'Final price: {d}')
