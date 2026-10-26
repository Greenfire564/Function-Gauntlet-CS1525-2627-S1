def is_even(number):
    """ Return True if number is even and False if it is odd.

    :param number:
    :return:
    """
    if number % 2==0:
        return True
    else:
        return False


def count_vowels(text):
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text:
    :return:
    """
    vowels = 0
    for letter in text.lower():
        if letter in "aeiou":
            vowels += 1
    return vowels


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius:
    :return:
    """
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def reverse_text(text):
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text:
    :return:
    """
    return text[::-1]



def larger_number(a, b):
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a:
    :param b:
    :return:
    """
    return a if a > b else b if a < b else a


def average_two(a, b):
    """Calculate and return the average of two integers.

    :param a:
    :param b:
    :return:
    """
    average = (a + b) / 2
    return average


def can_afford(balance, cost):
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance:
    :param cost:
    :return:
    """
    if balance >= cost:
        return True
    else:
        return False


def repeat_text(text, times):
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text:
    :param times:
    :return:
    """
    return text * times


def contains_word(sentence, word):
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence:
    :param word:
    :return:
    """
    if word in sentence:
        return True
    else:
        return False


def calculate_tip(cost, percent):
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost:
    :param percent:
    :return:
    """
    return cost * (percent / 100)



def make_initials(first_name, last_name):
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name:
    :param last_name:
    :return:
    """
    initials =  first_name[0].upper() + last_name[0].upper()
    return initials


def percent_score(points, possible):
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points:
    :param possible:
    :return:
    """
    if possible < 1:
        return None
    return points / possible * 100


def is_between(number, minimum, maximum):
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number:
    :param minimum:
    :param maximum:
    :return:
    """
    if number < minimum:
        return False
    elif number > maximum:
        return False
    else:
        return True


def all_different(a, b, c):
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a:
    :param b:
    :param c:
    :return:
    """
    return a != b and b != c and a != c


def average_three(a, b, c):
    """Calculate and return the average of three integers.

    :param a:
    :param b:
    :param c:
    :return:
    """
    average3 = (a + b + c) / 3
    return average3


def describe_temperature(temperature, cold_limit, hot_limit):
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature:
    :param cold_limit:
    :param hot_limit:
    :return:
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
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    pass

