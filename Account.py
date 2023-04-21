class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function increments account balance
        :param amount: specified amount
        :return: Either true or false whether deposit is (un)/successful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        """
        Function decreases account balance
        :param amount: specified amount
        :return: True or False whether deposit (un)/successful
        """

    def get_balance(self):
        pass

    def get_name(self):
        pass

    
