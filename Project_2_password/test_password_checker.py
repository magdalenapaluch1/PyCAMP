import pytest
from password_checker import Password_Checker

def test_password_too_short():

    password = "Polska1"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert safe_result is False

def test_password_non_digit():

    password = "PolskaPol"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert safe_result is False

def test_password_non_special_character():

    password = "Polskao1a"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert safe_result is False

def test_password_no_upper_character():

    password = "polskao1$a"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert safe_result is False

def test_password_no_lower_character():

    password = "POLSKA1@POL"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert safe_result is False
