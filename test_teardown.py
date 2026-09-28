import pytest
from bank import BankAccount

@pytest.fixture
def account():
    print("[setup]")

    acc = BankAccount(100)

    yield acc

    print("[teardown]")

def test_deposit(account):
    assert account.deposit(50) == 150

def test_withdraw(account):
    assert account.withdraw(30) == 70