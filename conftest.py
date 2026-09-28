import pytest
from bank import BankAccount


@pytest.fixture
def funded_account():
    """
    Return a BankAccount with balance 1000
    """
    return BankAccount(1000)