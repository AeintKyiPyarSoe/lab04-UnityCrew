import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150