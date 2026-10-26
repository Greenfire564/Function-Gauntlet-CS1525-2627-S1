def temperature_in_safe_range(celsius, minimum_f, maximum_f):
    """Convert Celsius to Fahrenheit and return True if
    the converted temperature is between the limits (inclusive).

    :param celsius:
    :param minimum_f:
    :param maximum_f:
    :return:
    """
    fahrenheit = (celsius * 9/5) + 32
    return minimum_f <= fahrenheit <= maximum_f

def can_afford_with_tip(balance, cost, tip_percent):
    """Calculate the tip, add it to the original cost, and
    return True if the balance can pay the complete total.

    :param balance:
    :param cost:
    :param tip_percent:
    :return:
    """
    total = cost + (cost * (tip_percent / 100))
    return balance >= total

def meets_average(score1, score2, score3, required_average):
    """Calculate the average of three scores and return True
    if it is greater than or equal to the required average.

    :param score1:
    :param score2:
    :param score3:
    :param required_average:
    :return:
    """
    average = (score1 + score2 + score3) / 3
    return average >= required_average

def initials_match(first_name, last_name, expected_initials):
    """Determine the initials of the first and last names
    and return True if they match expected_initials case-insensitively.

    :param first_name:
    :param last_name:
    :param expected_initials:
    :return:
    """
    actual_initials = first_name[0] + last_name[0]
    return actual_initials.upper() == expected_initials.upper()