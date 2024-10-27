class Node:
    def __init__(self, coef, exp):
        self.coefficient = coef
        self.exponent = exp
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coef, exp):
        new_term = Node(coef, exp)
        if not self.head:
            self.head = new_term
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_term

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            if current.next:
                print("+", end=" ")
            current = current.next
        print()

def add_polynomials(poly1, poly2):
    result = Polynomial()
    current1, current2 = poly1.head, poly2.head

    while current1 or current2:
        if not current1:
            result.insert_term(current2.coefficient, current2.exponent)
            current2 = current2.next
        elif not current2:
            result.insert_term(current1.coefficient, current1.exponent)
            current1 = current1.next
        else:
            if current1.exponent > current2.exponent:
                result.insert_term(current1.coefficient, current1.exponent)
                current1 = current1.next
            elif current1.exponent < current2.exponent:
                result.insert_term(current2.coefficient, current2.exponent)
                current2 = current2.next
            else:
                result.insert_term(current1.coefficient + current2.coefficient, current1.exponent)
                current1 = current1.next
                current2 = current2.next

    return result

def subtract_polynomials(poly1, poly2):
    result = Polynomial()
    current1, current2 = poly1.head, poly2.head

    while current1 or current2:
        if not current1:
            result.insert_term(-current2.coefficient, current2.exponent)
            current2 = current2.next
        elif not current2:
            result.insert_term(current1.coefficient, current1.exponent)
            current1 = current1.next
        else:
            if current1.exponent > current2.exponent:
                result.insert_term(current1.coefficient, current1.exponent)
                current1 = current1.next
            elif current1.exponent < current2.exponent:
                result.insert_term(-current2.coefficient, current2.exponent)
                current2 = current2.next
            else:
                result.insert_term(current1.coefficient - current2.coefficient, current1.exponent)
                current1 = current1.next
                current2 = current2.next

    return result

def multiply_polynomials(poly1, poly2):
    result = Polynomial()
    current1 = poly1.head

    while current1:
        current2 = poly2.head
        while current2:
            result.insert_term(current1.coefficient * current2.coefficient, current1.exponent + current2.exponent)
            current2 = current2.next
        current1 = current1.next

    return result

def divide_polynomials(poly1, poly2):
    result = Polynomial()
    current1 = poly1.head

    while current1:
        current2 = poly2.head
        while current2:
            if current2.coefficient != 0:  # Avoid division by zero
                result.insert_term(current1.coefficient / current2.coefficient, current1.exponent - current2.exponent)
            current2 = current2.next
        current1 = current1.next

    return result

# Function to take polynomial input from the user
def input_polynomial():
    poly = Polynomial()
    n = int(input("Enter the number of terms in the polynomial: "))
    for _ in range(n):
        coef = float(input("Enter the coefficient: "))
        exp = int(input("Enter the exponent: "))
        poly.insert_term(coef, exp)
    return poly

# Display menu
def display_menu():
    print("\nMenu:")
    print("1. Add Polynomials")
    print("2. Subtract Polynomials")
    print("3. Multiply Polynomials")
    print("4. Divide Polynomials")
    print("5. Exit")

# Main program
if __name__ == "__main__":
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            poly1 = input_polynomial()
            poly2 = input_polynomial()
            result = add_polynomials(poly1, poly2)
            print("Result of Addition:")
            result.display()

        elif choice == 2:
            poly1 = input_polynomial()
            poly2 = input_polynomial()
            result = subtract_polynomials(poly1, poly2)
            print("Result of Subtraction:")
            result.display()

        elif choice == 3:
            poly1 = input_polynomial()
            poly2 = input_polynomial()
            result = multiply_polynomials(poly1, poly2)
            print("Result of Multiplication:")
            result.display()

        elif choice == 4:
            poly1 = input_polynomial()
            poly2 = input_polynomial()
            result = divide_polynomials(poly1, poly2)
            print("Result of Division:")
            result.display()

        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-5).")
