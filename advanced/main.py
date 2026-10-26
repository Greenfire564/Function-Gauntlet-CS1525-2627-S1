def temperature_in_safe_range(celsius: float, minimum_f: float, maximum_f: float) -> bool:
    """Convert Celsius to Fahrenheit and check if it is between the limits.

    :param celsius: The temperature in Celsius.
    :param minimum_f: The lowest Fahrenheit limit.
    :param maximum_f: The highest Fahrenheit limit.
    :return: True if it is between the limits, False if not.
    """
    fahrenheit = (celsius * 9/5) + 32
    return minimum_f <= fahrenheit <= maximum_f


def can_afford_with_tip(balance: float, cost: float, tip_percent: float) -> bool:
    """Check if you have enough money to pay the cost plus a tip.

    :param balance: The money you have.
    :param cost: The base cost.
    :param tip_percent: The tip percent.
    :return: True if you have enough money, False if not.
    """
    total = cost + (cost * (tip_percent / 100))
    return balance >= total


def meets_average(score1: float, score2: float, score3: float, required_average: float) -> bool:
    """Check if the average of three scores meets the required average.

    :param score1: The first score.
    :param score2: The second score.
    :param score3: The third score.
    :param required_average: The minimum average needed.
    :return: True if the average is high enough, False if not.
    """
    average = (score1 + score2 + score3) / 3
    return average >= required_average


def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """Check if the initials of the names match the expected initials.

    :param first_name: The first name.
    :param last_name: The last name.
    :param expected_initials: The initials to check against.
    :return: True if they match, False if not.
    """
    actual_initials = first_name[0] + last_name[0]
    return actual_initials.upper() == expected_initials.upper()