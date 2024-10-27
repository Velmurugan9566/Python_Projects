#Real time Example: To track No of Customers Login the website
class Customer:

    count = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Customer.count += 1 #increment static value for each instance
    def cus_details(self):
        print("Name:",self.name)
        print("Email: ",self.email)
    def print_count(self):
        print("There are currently ",Customer.count," customers.")

# Create first customer instance
customer1 = Customer("Rajkumar", "Rk@example.com")
customer1.cus_details()
customer1.print_count()
print()
# Create second customer instance
customer2 = Customer("Anand", "Anand@example.com")
customer2.cus_details()
customer2.print_count()

#Access static variable from outside of the class
print("Total Customer: ",Customer.count)
