def cash(x):
    global balance
    cash_in=int(input("please insert cash:\t\t"))
    x=cash_in
    balance =balance + cash_in
    return cash_in

balance=0

cash(25)
print("asddf  ",balance)
cash(25)
print("new  ",balance)