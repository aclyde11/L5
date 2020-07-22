from goods import Item
from transaction import Transaction
from customer import Customer


class Store:
    def __init__(self, name_store):
        self.store_name = name_store

        self.customers = []
        self.items = []
        self.transactions = []


    '''
    
    given the itemname name, returns -1 if the itemname is not in the list
    otherwise, returns the index of the itemname in the list
    '''
    def find_item_in_store(self, itemname):
        for i in range(len(self.items)): # brute force search algorithm
            if itemname == self.items[i].name:
                return i
        return -1

    def find_customer_in_store(self, customername):
        for i in range(len(self.customers)): # brute force search algorithm
            if customername == self.customers[i].name:
                return i
        return -1

    '''
    itemname: is a string
    qty: is a quanty
    '''
    def stock(self, item, qty, price):
        idx = self.find_item_in_store(item)
        if  idx != -1:         # check if the itemname is already in stock, increment the quantity of the itemname
            self.items[idx].stock(qty)
        else:         # not if stock, create the itemname object and add it to our stock.
            item_obj = Item(item, price, qty)
            self.items.append(item_obj)

    def purchase(self, customername, itemname, qty, phone_number=None):
        ## Find or create new customer
        customer_idx = self.find_customer_in_store(customername)
        if customer_idx == -1:
            customer = Customer(customername, phone_number)
            self.customers.append(customer)
        else:
            customer = self.customers[customer_idx]

        ## Find the item they want to buy
        idx = self.find_item_in_store(itemname)


        if  idx != -1:         # check if the itemname is already in stock, increment the quantity of the itemname
            self.items[idx].purchase(qty)
            transaction = Transaction(customer, self.items[idx], qty)
            customer.add_dollars_spent(self.items[idx].price * qty)
            self.transactions.append(transaction)
        else:         # not if stock, create the itemname object and add it to our stock.
            raise ValueError("Trying to buy an itemname that is not in our store!")

    def summarize(self):
        print("Items in stock!")
        for item in self.items:
            print(f"NAME: {item.name}, QTY: {item.quantity}")
        print("\nCustomers")
        for customer in self.customers:
            print(f"NAME: {customer.name}, PTS: {customer.get_store_points()}")
