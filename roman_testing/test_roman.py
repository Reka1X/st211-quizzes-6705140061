from roman import convert


def test_single_digit():
    assert convert("I") == 1
    assert convert("V") == 5


def test_multiple_digits():
    assert convert("II") == 2
    assert convert("III") == 3


def test_different_digits():
    assert convert("VI") == 6
    assert convert("XVI") == 16


def test_subtractive_notation():
    assert convert("IV") == 4
    assert convert("IX") == 9
    assert convert("XL") == 40
    assert convert("XC") == 90


def test_digit_and_subtractive():
    assert convert("XIX") == 19