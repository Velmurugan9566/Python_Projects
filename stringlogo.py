from collections import Counter

def top_three_chars(input_str):
    char_count = Counter(input_str)
    print(char_count)
    sorted_chars = sorted(char_count.keys(), key=lambda char: (-char_count[char], char))
    print(sorted_chars)
    for char in sorted_chars[:3]:
        print(char, char_count[char])

# Read input from the user
input_str = input().strip().lower()

# Call the function to get the top three characters
top_three_chars(input_str)
