def print_parity(number):
    # Print the parity of the given number
    parity = number % 2
    print(f"Parity of {number} should be {parity}: {parity}")

def get_parity(number):
    # Return the parity of the given number
    return number % 2

def is_odd(number):
    # Check if the given number is odd and return True or False
    return number % 2 == 1

def main():
    print("Testing print_parity function:")
    print_parity(4)
    print_parity(41)

    print("\nTesting get_parity function:")
    parity_4 = get_parity(4)
    parity_41 = get_parity(41)
    print(f"Parity of 4 should be 0: {parity_4}")
    print(f"Parity of 41 should be 1: {parity_41}")

    print("\nTesting is_odd function:")
    age = int(input("Enter an age: "))
    if is_odd(age):
        print("Name in capitals")
    else:
        print("Name in lowercase")

if __name__ == "__main__":
    main()
