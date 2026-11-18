"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'
        if number % 2 == 0:
            conclusion += ' and even'
        else:
            conclusion += ' and odd'
        if number % 5 == 0:
            conclusion += ' and divisible by five'

    assert conclusion == 'Number bigger than or equal to one and divisible by five'


def test_if_multiple_elif_branches():
    """IF statement with multiple ELIF branches

    Conditions are checked from top to bottom and only the first branch whose condition is
    true runs. That is why the order of the elif branches matters.
    """

    def get_grade(score):
        # Check the highest range first so each elif only needs a lower bound.
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    # A score in the middle of each range picks that range's letter.
    assert get_grade(95) == 'A'
    assert get_grade(85) == 'B'
    assert get_grade(75) == 'C'
    assert get_grade(65) == 'D'
    assert get_grade(40) == 'F'

    # A score exactly on a boundary belongs to the higher grade, because >= is used.
    assert get_grade(90) == 'A'
    assert get_grade(60) == 'D'

    # A score just below a boundary falls through to the next branch.
    assert get_grade(89) == 'B'
    assert get_grade(59) == 'F'


def test_nested_if_statements():
    """Nested IF statements

    An if statement can be placed inside another if statement. The inner condition is only
    checked when the outer condition is true.
    """

    def get_ticket_price(age, is_weekend):
        # Children under 3 always go free, so the day is never checked for them.
        if age < 3:
            return 0
        elif age < 18:
            # Children pay more on weekends.
            if is_weekend:
                return 8
            else:
                return 6
        else:
            # Adults also pay more on weekends, and seniors get a discount on any day.
            if age >= 65:
                return 7
            elif is_weekend:
                return 15
            else:
                return 12

    # The outer condition alone decides the price for toddlers.
    assert get_ticket_price(2, is_weekend=True) == 0
    assert get_ticket_price(2, is_weekend=False) == 0

    # For children and adults, the nested condition on the day changes the price.
    assert get_ticket_price(10, is_weekend=True) == 8
    assert get_ticket_price(10, is_weekend=False) == 6
    assert get_ticket_price(30, is_weekend=True) == 15
    assert get_ticket_price(30, is_weekend=False) == 12

    # Seniors are matched by the first nested branch before the day is checked.
    assert get_ticket_price(70, is_weekend=True) == 7
    assert get_ticket_price(70, is_weekend=False) == 7
