from pytest import *
from Account import *

class Test:
    def setup_method(self):
        self.acc = Account('Jane')

    def teardown_method(self):
        del self.acc

    def test_init(self):
        assert self.acc.get_name() == 'Jane'
        assert self.acc.get_balance() == 0

    def test_deposit(self):
        #negative, zero, positive
        assert self.acc.deposit(-5) == False
        assert self.acc.get_balance() == 0
        assert self.acc.deposit(0) == False
        assert self.acc.get_balance() == 0
        assert self.acc.deposit(5) == True
        assert self.acc.get_balance() == 5

    def test_withdraw(self):
        #negative, zero, positive invalid
        assert self.acc.deposit(10)
        assert self.acc.withdraw(-5) == False
        assert self.acc.get_balance() == 10
        assert self.acc.withdraw(0) == False
        assert self.acc.get_balance() == 10
        assert self.acc.withdraw(50) == False
        assert self.acc.get_balance() == 10
        assert self.acc.withdraw(5) == True
        assert self.acc.get_balance() == 5



