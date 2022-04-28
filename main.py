class Item:
    pay_rate = 0.8  # pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# print(Item.__dict__)  # All attributes for Class level
# print(item1.__dict__)  # All attributes for Instance level
#
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
