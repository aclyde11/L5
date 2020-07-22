class Customer:
    '''
    Customer class encapsulates a customer in our store. It keeps track of the dollar amount they spend.
    '''
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.dollars_spent = 0

    '''
    increment the dollars the customer has spent in our store
    '''
    def add_dollars_spent(self, amount):
        self.dollars_spent += amount

    '''
    returns the points they have accumlated at our store.
    '''
    def get_store_points(self):
        return self.dollars_spent * 0.01
