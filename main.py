import os


class ProductManagement:
    def __init__(self, balance=0, product={}):
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
                product['name'] = input('Enter product name: ')
                product['bPrice'] = float(
                    input('Enter product buying price: '))
                product['sPrice'] = float(
                    input('Enter product selling price: '))
                product['qty'] = int(input('Input product quantity: '))
                product['profit'] = 0.0

                self.product[product['name']] = product

                print(
                    f"{product['qty']} {product['name']}{'s'*(product['qty']>1)} added successfully to inventory")
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
                keys = list(self.product)
                print('-'*50)
                print('-'*50)
                print('ID \t Product name')
                for i, key in enumerate(keys):
                    print(f'{i+1}\t   {key}')
                print('(Please enter product id to delete it.)')
                print('-'*50)
                print('-'*50)
                productId = int(input('Please enter product id: '))
                if productId < 1 or productId > len(keys):
                    print('Warning ! Product id out of range')
                    continue
                self.product.pop(keys[productId-1])
                print(
                    f"'{keys[productId-1]}' has been removed successfully from inventory")
                keys = list(self.product)
                print('-'*50)
                print('-'*50)
                print('ID \t Product name')
                for i, key in enumerate(keys):
                    print(f'{i+1}\t   {key}')
                print('Please enter product id to delete it.')
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
                keys = list(self.product)
                print('-'*50)
                print('-'*50)
                print('ID \t Product name')
                for i, key in enumerate(keys):
                    print(f'{i+1}\t   {key}')
                print('Please enter product id and quantity to buy.')
                print('-'*50)
                print('-'*50)
                productId = int(input('Please enter product id: '))
                if productId < 1 or productId > len(keys):
                    print('Warning ! Product id out of range')
                    continue
                qt = int(input('Please enter quantity: '))
                # print(self.product[keys[productId-1]])
                cost = qt * self.product[keys[productId-1]]['bPrice']
                print(cost, self.balance)
                # print('*'*10)
                if cost > self.balance:
                    print('Warning ! There is not enough to balance to buy ')
                else:
                    self.balance = self.balance - cost
                    self.product[keys[productId-1]
                                 ]['qty'] = self.product[keys[productId-1]]['qty'] + qt
                    print(f'Total cost of {qt} {keys[productId-1]}s = {cost}')
                    print(
                        f'{qt} {keys[productId-1]} {"s"*(qt>1)} bought successfully.')
                    print('-'*50)
                    print('-'*50)
            else:
                break

    def sellProduct(self):
        while(True):
            inp = int(input(
                '1.Sell a product\n2. Go To main menu\n(Enter the action number and press enter)\n'))
            if inp == 1:
                keys = list(self.product)
                print('-'*50)
                print('-'*50)
                header = '{:<5} {:<30} {:5}'.format(
                    "ID", "Product name", "Quantity")
                print(header)
                for i, key in enumerate(keys):
                    print('{:<5} {:<30} {:5}'.format(
                        i+1, key, self.product[key]['qty']))
                print('Please enter product id and quantity to sell.')
                print('-'*50)
                print('-'*50)
                productId = int(input('Please enter product id: '))
                if productId < 1 or productId > len(keys):
                    print('Warning ! Product id out of range')
                    continue
                qt = int(input('Please enter quantity: '))
                if qt > self.product[keys[productId-1]]['qty']:
                    print(
                        'There is not enough product in the\ninventory to meet the requirements')
                    continue
                profit = qt * \
                    (self.product[keys[productId-1]]['sPrice'] -
                     self.product[keys[productId-1]]['bPrice'])
                self.product[keys[productId-1]]['profit'] += profit
                self.product[keys[productId-1]]['qty'] -= qt
                self.balance += qt * self.product[keys[productId-1]]['sPrice']
                pName = self.product[keys[productId-1]]['name']
                print(f'Total {qt} {pName}{"s"*(qt>1)} sold')
                print(f'Total profit earned {profit}tk')
                print('-'*50)
                print('-'*50)
            else:
                break

    def showProductList(self):
        while(True):
            inp = int(input(
                '1.Product list\n2.Go To main menu\n(Enter the action number and press enter.)\n'))
            if inp == 1:
                keys = list(self.product)
                print('-'*50)
                print('-'*50)
                print()
                header = '|{:<5} {:<30} {:<8}  {:<10} |'.format(
                    'ID', 'Product name', 'Quantity', 'Profit')
                print("_"*len(header))
                print(header)
                print('|{:<5} {:<30} {:<8}  {:<10} |'.format(
                    '..', '....................', '........', '..........'))

                for i, key in enumerate(keys):
                    print('|{:<5} {:<30} {:<8}  {:<10} |'.format(
                        i+1, key, self.product[key]['qty'], self.product[key]['profit']))
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
        os.system('cls' if os.name == 'nt' else 'clear')
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
