"""
Python Logic Challenges
Author: [Seu Nome]
Purpose: Educational exercises focusing on logic, loops, and data structures.
"""

def reverse_string(text):
    """Challenge 1: Reverse a string without using built-in shortcuts like text[::-1]."""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def fizz_buzz(n):
    """Challenge 2: Standard FizzBuzz algorithm using conditional logic."""
    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results

def count_vowels(text):
    """Challenge 3: Count the number of vowels in a string using dictionary/sets."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    # Test Challenge 1
    print("1. Reversing 'python':", reverse_string("python"))
    
    # Test Challenge 2
    print("2. FizzBuzz up to 15:", fizz_buzz(15))
    
    # Test Challenge 3
    print("3. Vowels in 'Artificial Intelligence':", count_vowels("Artificial Intelligence"))
