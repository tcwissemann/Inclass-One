def add_numbers(x, y):
    return_value = x + y
    return return_value

def multiply_numbers(x, y):
    return_value = 0
    for i in range(y):
        return_value += x
    return return_value

def multiply_number_by_11(x):
    return x * 11

def main():
    # logic
    addition = add_numbers(4, 5)
    multiplication = multiply_numbers(4, 5)
    multiplication_by_11 = multiply_number_by_11(4)

    print(f"4 + 5 = {addition}, 4 * 5 = {multiplication}, 4 * 11 = {multiplication_by_11}")

    if addition == 9 and multiplication == 20 and multiplication_by_11 == 44:
        print("All tests pass ✅")
    else:
        print("At least one test failed ❌")

if __name__ == "__main__":
    main()