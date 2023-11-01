import random

# Coffee Style Calculator Functions
def calculate_coffee_ratio(dose, yield_):
    return yield_ / dose

def determine_coffee_style(ratio):
    if ratio < 1:
        return "ristretto"
    elif ratio >= 1 and ratio < 2:
        return "normale"
    elif ratio >= 2 and ratio < 3:
        return "lungo"
    else:
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

# Parity Functions
def print_parity(number):
    parity = number % 2
    print(f"Parity of {number} should be {parity}: {parity}")

def get_parity(number):
    return number % 2

def is_odd(number):
    return number % 2 == 1

# JCU Grades Functions
def determine_jcu_grade(score):
    if score < 50:
        return "F"
    elif score >= 50 and score < 65:
        return "P"
    elif score >= 65 and score < 75:
        return "C"
    elif score >= 75 and score < 85:
        return "D"
    else:
        return "HD"

def test_jcu_grades():
    assert determine_jcu_grade(49) == "F"
    assert determine_jcu_grade(50) == "P"
    assert determine_jcu_grade(64) == "P"
    assert determine_jcu_grade(65) == "C"
    assert determine_jcu_grade(74) == "C"
    assert determine_jcu_grade(75) == "D"
    assert determine_jcu_grade(84) == "D"
    assert determine_jcu_grade(85) == "HD"
    assert determine_jcu_grade(100) == "HD"

# Main Program
def main():
    while True:
        print("Choose an option:")
        print("1. Coffee Style Calculator")
        print("2. Parity Program")
        print("3. JCU Grades Program")
        print("4. Quit")
        option = input("Enter your choice: ")
        
        if option == "1":
            dose = get_valid_number("Enter the dose (grams): ")
            yield_ = get_valid_number("Enter the yield (grams): ")
            ratio = calculate_coffee_ratio(dose, yield_)
            style = determine_coffee_style(ratio)
            print(f"{dose}:{yield_} is considered {style} coffee style")
        elif option == "2":
            number = float(input("Enter a number: "))
            print_parity(number)
        elif option == "3":
            while True:
                score = float(input("Enter a subject total score (or a negative value to exit): "))
                if score < 0:
                    break
                grade = determine_jcu_grade(score)
                print(f"The score {score} is {grade}")
                
            num_random_scores = int(input("How many random scores: "))
            for _ in range(num_random_scores):
                random_score = random.uniform(0, 100)
                grade = determine_jcu_grade(random_score)
                print(f"{int(random_score)} = {grade}")
        elif option == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
