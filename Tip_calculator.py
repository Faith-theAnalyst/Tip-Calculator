#import locale
#locale.setlocale(locale.LC_ALL, '')
name = ("Asanka Hotel Tip Calculator")
print(name.title())
#Charge of the food
charge = float(input("Enter the charge for the food: $"))

#Calculate 18% tip on the charge of food
tip = charge * 0.18

#Calculate 7% sales tax on charge of food
sales_tax = charge * 0.07

#Total amount incurred (Charge+Tip+Sales tax)
total_charge = charge + tip + sales_tax

# display the tip amount
print("Tip = $%.2f" % tip)

# display the sales tax amount
print("Sales tax = $%.2f" % sales_tax)

# display the grand total
print("Grand total = $%.2f" % total)

#print("tip = ${:.2f}".format(tip))
#print("sales_tax = ${:.2f}".format(sales_tax))
#print("total_charge = ${:.2f}".format(total_charge))

#print(f'tip = {locale.currency(tip)}')
#print(f'sales_tax = {locale.currency(sales_tax)}')
#print(f'total_charge = {locale.currency (total_charge)}')







