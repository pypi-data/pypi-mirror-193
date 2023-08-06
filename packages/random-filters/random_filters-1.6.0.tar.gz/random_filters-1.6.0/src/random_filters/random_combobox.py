from random import choice, randint
from pandas import DataFrame


def combobox_hierarchy(data: dict | DataFrame) -> str:
    """
    Generate a random combobox with hierarchy.

    :param data: A dict or DataFrame with the data.
    :return: A random combobox between the present combobox.
    :rtype: str
    :Example:
        >>> combobox_hierarchy({"Estado": ["SP", "SP", "SP", "SC", "SC", "SC"],
        >>> "Cidade": ["São Paulo", "Itatiba", "Campinas", "Chapecó", "Xaxim", "Xanxerê"]})
    """
    if not isinstance(data, dict | DataFrame):
        raise TypeError('The data must be a dict or DataFrame')

    df = data if isinstance(data, DataFrame) else DataFrame(data)
    check_hierarchy(df)
    first, second = set_choices(df)
    return f'{df.columns[0]} {first} e {df.columns[1]} {second}'


def set_choices(df: DataFrame) -> tuple[str, str]:
    """
    Set the choices of the combobox.
    :param df: A DataFrame with the data.
    :return: A tuple with the choices.
    :rtype: tuple[str, str]
    :Example:
        >>> set_choices(df)
    """
    first: str = choice(df.iloc[:, 0])
    df: DataFrame = df[df.iloc[:, 0] == first]
    second: str = df.iloc[randint(0, len(df) - 1), 1]
    return first, second


def check_hierarchy(df: DataFrame) -> None:
    """
    Check if the DataFrame has hierarchy.
    :param df: A DataFrame with the data.
    :return: None
    :raises ValueError: If the DataFrame does not have hierarchy.
    :Example:
        >>> check_hierarchy(df)
    """
    assert len(df.iloc[:, 0]) != len(set(df.iloc[:, 0])), 'The DataFrame must have hierarchy'
