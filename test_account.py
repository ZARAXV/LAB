from pytest import *
from Account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John', 10)
        self.a2 = Account('John', 20)

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        pass

    def test_deposit(self):
        #negative, zero, positive
        pass

    def test_withdraw(self):
        #negative, zero, positive invalid, positve invalid
        pass
