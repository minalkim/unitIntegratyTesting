import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility


# ---------------- Deposit Tests ----------------
def test_deposit_valid():
    assert deposit(1000, 500) == 1500

def test_deposit_boundary():
    assert deposit(0, 1) == 1

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, 0)


# ---------------- Withdraw Tests ----------------
def test_withdraw_valid():
    assert withdraw(1000, 300) == 700

def test_withdraw_boundary():
    assert withdraw(500, 500) == 0

def test_withdraw_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(500, -10)

def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(500, 600)


# ---------------- Interest Tests ----------------
def test_calculate_interest_valid():
    result = calculate_interest(1000, 10, 2)
    assert round(result, 2) == 1210.00

def test_calculate_interest_zero_years():
    assert calculate_interest(1000, 10, 0) == 1000

def test_calculate_interest_invalid_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 1)

def test_calculate_interest_invalid_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 1)


# ---------------- Loan Eligibility Tests ----------------
def test_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True

def test_loan_not_eligible_low_balance():
    assert check_loan_eligibility(3000, 750) is False

def test_loan_not_eligible_low_score():
    assert check_loan_eligibility(6000, 650) is False

def test_loan_invalid_balance():
    with pytest.raises(ValueError):
        check_loan_eligibility(-100, 700)
