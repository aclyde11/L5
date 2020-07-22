class Transaction:
    '''
    This class represents a transaction that occured in our store.
    '''
    def __init__(self, customer, item, qty):
        self.customer = customer
        self.item = item
        self.qty = qty