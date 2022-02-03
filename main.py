import os


class Item:
    def __init__(self, name, bPrice, sPrice, quantity, profit=0.0):
        self.name = name
        self.bPrice = bPrice
        self.sPrice = sPrice
        self.qty = quantity
        self.profit = profit

    def getName(self):
        return self.name

    def getbPrice(self):
        return self.bPrice

    def getsPrice(self):
        return self.sPrice

    def getQuantity(self):
        return self.qty

    def getProfit(self):
        return self.profit

    def setQuantity(self, quantity):
        self.qty = quantity

    def setProfit(self, profit):
        self.profit = profit

    def calcGain(self):
        return self.sPrice - self.bPrice


class ProductManagement:
    def __init__(self, balance=0, product=[]):
        self.balance = balance
        self.product = product

    def addProduct(self):
        print('-'*50)
        print('-'*50)
        print()
        while(True):
            inp = int(input(
                '1. Add a product to inventory\n2. Go To main menu\n(Enter the action number and press enter)\n'))
            if inp == 1:
                product = {}
                pName = input('Enter product name: ')
                flag = 0
                for i in self.product:
                    if pName == i.getName():
                        print(
                            'Warning !!!\nThis product already exists in the inventory.\nGo to main menu and check inventory for details')
                        flag += 1
                        break
                if flag != 0:
                    continue
                buyingPrice = float(
                    input('Enter product buying price: '))
                sellingPrice = float(
                    input('Enter product selling price: '))
                quantity = int(input('Input product quantity: '))
                newProduct = Item(pName, buyingPrice, sellingPrice, quantity)

                self.product.append(newProduct)

                print(
                    f"{quantity} {pName}{'s'*(quantity>1)} added successfully to inventory")
                print()
                print('-'*50)
                print('-'*50)
            else:
                break

    def deleteProduct(self):
        print('-'*50)
        print('-'*50)
        print()
        while(True):
            inp = int(input(
                '1.Delete a product\n2. Go To main menu\n(Enter the action number and press enter)\n'))
            if inp == 1:
                print('-'*50)
                print('-'*50)
                if len(self.product) > 0:
                    print('ID \t Product name')
                    for i, prod in enumerate(self.product):
                        print(f'{i+1}\t   {prod.name}')
                    print(
                        '(Please enter product id to delete.)')
                else:
                    print(
                        'There is no product to delete.\n Please add product first then come back.')
                    continue
                print('-'*50)
                print('-'*50)
                productId = int(input('Please enter product id: '))
                if productId < 1 or productId > len(self.product):
                    print('Warning ! Product id out of range')
                    continue
                popItem = self.product.pop(productId-1)
                print(
                    f"'{popItem.name}' has been removed successfully from inventory")
                # keys = list(self.product)
                print('-'*50)
                print('-'*50)
                print('ID \t Product name')
                for i, prod in enumerate(self.product):
                    print(f'{i+1}\t   {prod.name}')
                print('-'*50)
                print('-'*50)
            else:
                break

    def buyProduct(self):
        print('-'*50)
        print('-'*50)
        print()
        while(True):
            inp = int(input(
                '1.Buy a product\n2. Go To main menu\n(Enter the action number and press enter)\n'))
            if inp == 1:
                # keys = list(self.product)
                print('-'*50)
                print('-'*50)
                # print('ID \t Product name \t Buying Price')
                if len(self.product) > 0:
                    print('{:<4} {:<30} {:<20}'.format(
                        "Id", "Product name", "Buying Price"))
                    for i, prod in enumerate(self.product):
                        print('{:<4} {:<30} {:<20}'.format(
                            i+1, prod.getName(), prod.getbPrice()))
                else:
                    print(
                        'There is no product to buy.\nPlease add product first then come back')
                    continue
                    # print(f'{i+1}\t   {prod.getName()} \t {prod.getbPrice()}')
                print()
                print('Please enter product id and quantity to buy.')
                print('-'*50)
                print('-'*50)
                productId = int(input('Please enter product id: '))
                if productId < 1 or productId > len(self.product):
                    print('Warning ! Product id out of range')
                    continue
                qt = int(input('Please enter quantity: '))
                # print(self.product[keys[productId-1]])
                cost = qt * self.product[productId-1].getbPrice()
                # print(cost, self.balance)
                # print('*'*10)
                if cost > self.balance:
                    print('Warning ! There is not enough to balance to buy ')
                else:
                    self.balance = self.balance - cost
                    newQuantity = self.product[productId-1].getQuantity() + qt
                    self.product[productId-1].setQuantity(newQuantity)
                    # self.product[keys[productId-1]
                    #              ]['qty'] = self.product[keys[productId-1]]['qty'] + qt
                    print(
                        f'Total cost of {qt} {self.product[productId-1].getName()}s = {cost}')
                    print(
                        f'{qt} {self.product[productId-1].getName()} {"s"*(qt>1)} bought successfully.')
                    print('-'*50)
                    print('-'*50)
            else:
                break

    def sellProduct(self):
        while(True):
            inp = int(input(
                '1.Sell a product\n2. Go To main menu\n(Enter the action number and press enter)\n'))
            if inp == 1:
                # keys = list(self.product)
                print('-'*50)
                print('-'*50)
                if len(self.product) > 0:
                    header = '{:<5} {:<30} {:5}'.format(
                        "ID", "Product name", "Quantity")
                    print(header)
                    for i, key in enumerate(self.product):
                        print('{:<5} {:<30} {:5}'.format(
                            i+1, self.product[i].getName(), self.product[i].getQuantity()))
                    print('Please enter product id and quantity to sell.')
                else:
                    print(
                        'There is product to sell.\nGo to main menu and add new product\n')
                    continue
                print('-'*50)
                print('-'*50)
                productId = int(input('Please enter product id: '))
                if productId < 1 or productId > len(self.product):
                    print('Warning ! Product id out of range')
                    continue
                qt = int(input('Please enter quantity: '))
                if qt > self.product[productId-1].getQuantity():
                    print(
                        'There is not enough product in the\ninventory to meet the requirements')
                    continue
                # profit = qt * \
                #     (self.product[keys[productId-1]]['sPrice'] -
                #      self.product[keys[productId-1]]['bPrice'])
                totalProfit = (self.product[productId-1].calcGain() * qt)
                self.product[productId-1].setProfit(
                    totalProfit + self.product[productId-1].getProfit())
                # self.product[keys[productId-1]]['qty'] -= qt
                newQuantity = self.product[productId-1].getQuantity() - qt
                self.product[productId-1].setQuantity(newQuantity)

                self.balance += qt * self.product[productId-1].getsPrice()
                # pName = self.product[productId-1].getName()
                print(
                    f'Total {qt} {self.product[productId-1].getName()}{"s"*(qt>1)} sold')
                print(f'Total profit earned {totalProfit}tk')
                print('-'*50)
                print('-'*50)
            else:
                break

    def showProductList(self):
        while(True):
            inp = int(input(
                '1.Product list\n2.Go To main menu\n(Enter the action number and press enter.)\n'))
            if inp == 1:
                # keys = list(self.product)
                print('-'*50)
                print('-'*50)
                print()
                if len(self.product) > 0:
                    header = '|{:<5} {:<30} {:<8}  {:<10} |'.format(
                        'ID', 'Product name', 'Quantity', 'Profit')
                    print("_"*len(header))
                    print(header)
                    print('|{:<5} {:<30} {:<8}  {:<10} |'.format(
                        '..', '....................', '........', '..........'))

                    for i, key in enumerate(self.product):
                        print('|{:<5} {:<30} {:<8}  {:<10} |'.format(
                            i+1, self.product[i].getName(), self.product[i].getQuantity(), self.product[i].getProfit()))
                else:
                    print(
                        'There is no product in the inventory to show !!!\nGo to main menu to add product.')
                    print()
                    print('-'*50)
                    continue
                print("_"*len(header))
                print()
                print('-'*50)
                print('-'*50)
            else:
                break

    def showBalance(self):
        while(True):
            inp = int(input(
                '1.Total balance\n2.Go To main menu\n(Enter the action number and press enter.)\n'))
            if inp == 1:
                print('-'*50)
                print('-'*50)
                print()
                print(f'Available total balance is {self.balance} tk')
                print()
                print('-'*50)
                print('-'*50)
            else:
                break


def main():

    businessman = ProductManagement()

    while(True):
        # os.system('cls' if os.name == 'nt' else 'clear')
        print('-'*50)
        print('-'*50)
        print()
        option = int(input('1.Add a product\n2.Delete a product\n3.Buy a product\n4.Sell a product\n5.See list of product\n6.See available balance\n7.Quit\n(Enter number of the action and press enter)\n'))
        if option == 1:
            businessman.addProduct()
        elif option == 2:
            businessman.deleteProduct()
        elif option == 3:
            businessman.buyProduct()
        elif option == 4:
            businessman.sellProduct()
        elif option == 5:
            businessman.showProductList()
        elif option == 6:
            businessman.showBalance()
        else:
            break
        print('-'*50)
        print('-'*50)


if __name__ == "__main__":
    main()
