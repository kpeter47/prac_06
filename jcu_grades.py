import random

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
    # Test cases for all possible grade boundaries
    assert determine_jcu_grade(49) == "F"
    assert determine_jcu_grade(50) == "P"
    assert determine_jcu_grade(64) == "P"
    assert determine_jcu_grade(65) == "C"
    assert determine_jcu_grade(74) == "C"
    assert determine_jcu_grade(75) == "D"
    assert determine_jcu_grade(84) == "D"
    assert determine_jcu_grade(85) == "HD"
    assert determine_jcu_grade(100) == "HD"

def main():
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

if __name__ == "__main__":
    test_jcu_grades()  # Run the test function
    main()  # Run the main program
