def print_even_number(arr):

    found_even = False

    for num in arr:
        if num % 2 == 0:
            print(num)

            found_even = True


    if found_even == False:
        print("There are no even numbers.")


# --- Test Cases ---

print("Test 1 (Mixed numbers):")
example_input = [3, 8, 12, 5, 7, 14]
print_even_number(example_input)

print("\nTest 2 (Only odd numbers):")
odd_input = [1, 3, 5, 7, 9]
print_even_number(odd_input)


def linearSearch(array, target):

    for i in range(len(array)):

        if array[i] == target:
            return i


    return -1



my_array = [15, 22, 8, 93, 41]

print("\nQuestion 6 Output:")

target_1 = 8
print(f"Index of {target_1}: {linearSearch(my_array, target_1)}")


target_2 = 100
print(f"Index of {target_2}: {linearSearch(my_array, target_2)}")