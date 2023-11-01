def determine_coffee_style(ratio):
    if ratio >= 1 and ratio <= 2:
        return "ristretto"
    elif ratio > 2 and ratio <= 3:
        return "normale"
    elif ratio > 3 and ratio <= 4:
        return "lungo"
    else:
        # Handle cases outside the defined ranges
        if ratio < 1:
            return "ristretto"
        elif ratio > 4:
            return "lungo"

def get_valid_number(prompt, max_value=100):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between 0 and {max_value}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Coffee Style Calculator!")
    dose = get_valid_number("Enter the dose (grams): ")
    yield_ = get_valid_number("Enter the yield (grams): ")
    ratio = yield_ / dose
    style = determine_coffee_style(ratio)
    print(f"{dose}:{yield_} is considered {style} coffee style")

if __name__ == "__main__":
    main()
