def count_vowels(text):
    # 1. Define the vowels to look for
    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = {}

    # 2. Loop through the input 'text' (converted to lowercase)
    for char in text.lower():
        if char in vowels:
            # 3. Update count for that specific vowel
            counts[char] = counts.get(char, 0) + 1

    # 4. Return the final dictionary so we can use it outside the function
    return counts


# --- Testing the code ---
input_string = "Hello Worldaaaa"
result = count_vowels(input_string)

print(result)
# ALGORITHM:
# 1. Provide a string of text and a set of characters defined as vowels.
# 2. Initialize an empty dictionary to store the individual counts.
# 3. Normalize the text by converting it to lowercase.
# 4. Iterate through every character in the text one by one.
# 5. Check if the character is a vowel.
# 6. If it is a match,update count for that specific vowel.
# 7. Continue until every character in the string has been processed.
# 8. Return or print the final results.