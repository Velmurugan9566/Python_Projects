def generate_series(a, b):
    result = []
    for i in range(a, a + 10):
        for j in range(b, b + 2):
            result.append(int(str(i) + str(j)))
    return result

# Get user input
input_a = int(input("Enter the first number: "))
input_b = int(input("Enter the second number: "))

# Generate and print the series
series = generate_series(input_a, input_b)
print("Generated Series:", series)
