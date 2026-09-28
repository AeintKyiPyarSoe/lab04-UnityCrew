import pytest


def test_deposit(funded_account):
    assert funded_account.deposit(100) == 1100


def test_withdraw(funded_account):
    assert funded_account.withdraw(100) == 900


def test_withdraw_insufficient_funds(funded_account):
    with pytest.raises(ValueError, match="Insufficient funds."):
        funded_account.withdraw(1100)