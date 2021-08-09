invoices = open('CupcakeInvoices.csv')

all_total = 0
for total in invoices:
    total = total.rstrip('\r\n').split(',')
    #round(total, 2)
    last = float(total[-1])
    second_last = int(total[-2])
    mult = last * second_last
    f = float(total[-1])
    all_total += mult
    print(all_total)
    #print(last)
    
invoices.close()