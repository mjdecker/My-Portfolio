from money import Money 

class USA(Money) :
    def __init__(self, amount='0'):
        super().__init__(amount=amount, currency='USA')

    def format(self) :
        return '$' + super().format('en_US')[3: ]

    def __str__(self) :
        return self.format()