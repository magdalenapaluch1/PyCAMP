import pytest
from password_checker import Password_Checker

def test_password_too_short():

    password = "Polska1"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert "too_short" in safe_result

def test_password_non_digit():

    password = "PolskaPol"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert "no_digit" in safe_result

def test_password_non_special_character():

    password = "Polskao1a"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert "no_special" in safe_result

def test_password_no_upper_character():

    password = "polskao1$a"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert "no_upper" in safe_result

def test_password_no_lower_character():

    password = "POLSKA1@POL"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert "no_lower" in safe_result

def test_safe_password():

    password = "Polska12@"
    pc = Password_Checker()
    safe_result = pc.is_password_safe(password)

    assert "password_safe" in safe_result