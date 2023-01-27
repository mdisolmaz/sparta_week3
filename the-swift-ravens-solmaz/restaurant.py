class Table:

    def __init__(self, diners):
        self.diners = diners
        self.bill = []


# (def order) Accepts an item, price and a quantity. 
# If the item already exists in the bill, the quantity is updated, 
# otherwise a new item is added to the bill.

    def order(self, item, price, quantity=1):
        for i in self.bill:
            if i['item'] == item and i['price'] == price:
                i['quantity'] += quantity
        self.bill.append({'item': item, 'price': price, 'quantity': quantity})

# Takes in an item, its price, and  a quantity.
# If the item is already exists in the bill
# it removes the item from the bill
        
    def remove(self, item, price, quantity=1):
        for i in self.bill:
            if i['item'] == item and i['price'] == price:
                i['quantity'] -= quantity
                if i['quantity'] <= 0:
                    self.bill.remove(i)
                return True
        return False

# Calculates the subtotal for the bill by multiplying 
# the price and quantity for each item in the bill


    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            subtotal += i['price'] * i['quantity']
        return subtotal
    

# Accepts service charge as a decimal
# and returns a dictionary with the subtotal,
# service charge and total amount


    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        service_charge_amount = subtotal * service_charge
        total = subtotal + service_charge_amount
        return {
            'Sub Total': '£{:.2f}'.format(subtotal),
            'Service Charge': '£{:.2f}'.format(service_charge_amount),
            'Total': '£{:.2f}'.format(total)
        }
    
# Returns the subtotal of the bill divided by the number of diners
# rounded up to the nearest pence

    def split_bill(self):
        return round(self.get_subtotal() / self.diners, 2)
    
########################################################################