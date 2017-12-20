def inputCustName():
    name = input('Enter the customer name: ')
    nameParts = name.split()
    return nameParts

def inputCustBalance():
    custBalance = float(input('Enter customer balance: '))
    if custBalance >= 0:
        balanceType = 'Non-negative'
    else:
        balanceType = 'Negative'
    return custBalance, balanceType

def main():
    custName = inputCustName()
    custBal, balType = inputCustBalance()
    print('Customer name    = ' + str(custName[0]))
    print('Customer balance = ' + format(custBal, '.2f') + ', ' + balType)

main()
