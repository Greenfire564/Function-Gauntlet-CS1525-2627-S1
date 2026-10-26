def is_even(number: int) -> bool:
    """Check if a number is even.

    :param number: The number to check.
    :return: True if it is even, False if it is odd.
    """
    if number % 2 == 0:
        return True
    else:
        return False


def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in the text.

    :param text: The text to check.
    :return: The total number of vowels.
    """
    vowels = 0
    for letter in text.lower():
        if letter in "aeiou":
            vowels += 1
    return vowels


def celsius_to_fahrenheit(celsius: float) -> float:
    """Change Celsius temperature to Fahrenheit.

    :param celsius: The temperature in Celsius.
    :return: The temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def reverse_text(text: str) -> str:
    """Flip the text backward.

    Example:
        "robot" becomes "tobor"

    :param text: The text to flip.
    :return: The text in reverse order.
    """
    return text[::-1]


def larger_number(a: int, b: int) -> int:
    """Find the bigger number.

    :param a: The first number.
    :param b: The second number.
    :return: The bigger number.
    """
    return a if a > b else b if a < b else a


def average_two(a: int, b: int) -> float:
    """Find the middle value of two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: The average of the two numbers.
    """
    average = (a + b) / 2
    return average


def can_afford(balance: float, cost: float) -> bool:
    """Check if you have enough money.

    :param balance: The money you have.
    :param cost: How much it costs.
    :return: True if you have enough, False if not.
    """
    if balance >= cost:
        return True
    else:
        return False


def repeat_text(text: str, times: int) -> str:
    """Repeat text a certain number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: The text to repeat.
    :param times: How many times to repeat it.
    :return: The repeated text.
    """
    return text * times


def contains_word(sentence: str, word: str) -> bool:
    """Check if a word is inside a sentence.

    :param sentence: The text to look in.
    :param word: The word to find.
    :return: True if the word is there, False if not.
    """
    if word in sentence:
        return True
    else:
        return False


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate the tip money.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: The total price.
    :param percent: The tip percent.
    :return: The tip amount.
    """
    return cost * (percent / 100)


def make_initials(first_name: str, last_name: str) -> str:
    """Get the first letter of two names in uppercase.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: The first name.
    :param last_name: The last name.
    :return: The two letters in uppercase.
    """
    initials = first_name[0].upper() + last_name[0].upper()
    return initials


def percent_score(points: float, possible: float) -> float | None:
    """Calculate test score as a percentage.

    Example:
        18 out of 20 returns 90.0.

    :param points: Points you got.
    :param possible: Total points possible.
    :return: The score as a percent, or None if possible is less than 1.
    """
    if possible < 1:
        return None
    return points / possible * 100


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Check if a number is between two limits.

    :param number: The number to check.
    :param minimum: The lowest limit.
    :param maximum: The highest limit.
    :return: True if it is between them, False if not.
    """
    if number < minimum:
        return False
    elif number > maximum:
        return False
    else:
        return True


def all_different(a: str, b: str, c: str) -> bool:
    """Check if three texts are all different.

    :param a: The first text.
    :param b: The second text.
    :param c: The third text.
    :return: True if all are different, False if any match.
    """
    return a != b and b != c and a != c


def average_three(a: int, b: int, c: int) -> float:
    """Find the middle value of three numbers.

    :param a: The first number.
    :param b: The second number.
    :param c: The third number.
    :return: The average of the three numbers.
    """
    average3 = (a + b + c) / 3
    return average3


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """Describe how the temperature feels.

    :param temperature: The current temperature.
    :param cold_limit: The limit for cold.
    :param hot_limit: The limit for hot.
    :return: "cold", "hot", or "comfortable".
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"


if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    """
    pass