from bank import BankAccount

def test_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150