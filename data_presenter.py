invoices = open('CupcakeInvoices.csv')

all_total = 0
for total in invoices:
    total = total.rstrip('\r\n').split(',')
    last = float(total[-1])
    second_last = int(total[-2])
    mult = last * second_last
    print(round(mult, 2))
    
invoices.close()

#graph

import matplotlib.pyplot as plt

cupcake_invoices = open('CupcakeInvoices.csv')

chocolate_income = 0
strawberry_income = 0
vanilla_income = 0 

for line in cupcake_invoices:
    line = line.rstrip('\n').split(',')
    if line[2] == "Chocolate":
        chocolate_income += round(int(line[3]) * float(line[4]))
    elif line[2] == "Strawberry":
        strawberry_income += round(int(line[3]) * float(line[4]))
    elif line[2] == "Vanilla":
        vanilla_income += round(int(line[3]) * float(line[4]))

data = {
    "Chocolate": chocolate_income,
    "Strawberry": strawberry_income,
    "Vanilla": vanilla_income
}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5))

plt.bar(courses, values, color='maroon', width=0.4)

plt.xlabel("Types of cupcakes offered")
plt.ylabel("total sales")
plt.title("Total Python Cupcakes sales")
plt.show()