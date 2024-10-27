from abc import ABC, abstractmethod

# Abstract Shop class
class Shop(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_menu(self):
        pass
        

    @abstractmethod
    def make_bill(self, order):
        pass

# Derived class Mobile_Shop
class Mobile_Shop(Shop):
    def __init__(self, name):
        super().__init__(name)

    def show_menu(self):
        return "Mobiles, Accessories, and Gadgets Menu"

    def make_bill(self, order):
        return f"{self.name} - Bill: ${order}"

# Derived class Coffee_Shop
class Coffee_Shop(Shop):
    def __init__(self, name):
        super().__init__(name)

    def show_menu(self):
        return "Coffee and Beverages Menu\n1.coffe corner"

    def make_bill(self, order):
        return f"{self.name} - Bill: ${order}"

# Derived class Cake_Shop
class Cake_Shop(Shop):
    def __init__(self, name):
        super().__init__(name)

    def show_menu(self):
        return "Cakes and Pastries Menu"

    def make_bill(self, order):
        return f"{self.name} - Bill: ${order}"

# Polymorphic function to display menu and make a bill
def visit_shop(shop):
    print(shop.show_menu())
    order = 50             # Example order amount
    print(shop.make_bill(order))

# Create instances of different shop types
mobile_shop = Mobile_Shop("Gadget Galaxy")
coffee_shop = Coffee_Shop("Coffee Corner")
cake_shop = Cake_Shop("Sweet Delights")

# Visit and interact with each shop
visit_shop(mobile_shop)
visit_shop(coffee_shop)
visit_shop(cake_shop)
