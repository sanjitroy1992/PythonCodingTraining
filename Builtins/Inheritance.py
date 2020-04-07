class Employee:
    raise_amount = 1.1

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name + '.' + self.last_name + '@gmail.com'
        self.pay = pay

    def pay_raise(self):
        return int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.5
    # pass


dev1 = Developer('Sanjit', 'Roy', 50000)
print(dev1.pay)
print(dev1.pay_raise())