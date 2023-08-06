from random import choice, randint


def get_random_checkbox(checkboxes=None, probability=0.5):
    """
    Returns a random checkbox from the given list of checkboxes with a given probability.

    :param checkboxes: A list of checkbox options (default: None).
    :type checkboxes: list of str

    :param probability: The probability of returning a checkbox (default: 0.5).
    :type probability: float

    :return: A random checkbox from the given list or an empty string if no checkbox is selected.
    :rtype: str
    """
    if checkboxes is None:
        checkboxes = ['almoco', 'jantar', 'final de semana', 'dia de semana']

    probability = min(max(probability, 0), 1)

    return choice(checkboxes) if randint(0, 100) / 100 <= probability else ''
