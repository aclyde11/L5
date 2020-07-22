class Item:
    '''
    This class encapsulates a itemname in our store
    '''
    def __init__(self, name, price, quantity = 1):
        self.name = name
        self.quantity = quantity
        self.price = price


    '''
    This function decrements the quantity in stock. If qty is greater than the quanity in stock, an
    error is thrown.
    '''
    def purchase(self, qty=1):
        if self.quantity - qty < 0:
            raise ValueError("Error! Trying to buy more than we have in stock.")
        self.quantity -= qty

    '''
    This function increments the quantity in stock
    '''
    def stock(self, qty=1):
        self.quantity += qty



class PerishableItem(Item):
    '''
    This class encapsulates a perhisable itemname in our store
    TODO add in a perishable date, and remove the itemname from our stock when it expires.
    '''
    def __init__(self, name, qty=1):
        super().__init__(name, qty)