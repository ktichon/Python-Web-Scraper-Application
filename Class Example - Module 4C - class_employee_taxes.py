class Employee():
    """Employee info and tax calculations."""
    def __init__(self, id, name, income):
        """Init function."""
        self.name = name
        self.id = id
        self.income = income
        # the self variables will be unique to each class instatiated

    def income_taxes(self):
        """Calculates taxes based on income."""
        rate = 0.20
        return rate * self.income


employee1 = Employee(1234, "Gru Badguy", 99000)
employee2 = Employee(2222, "Agnes Teenager", 49000)

print(employee1.name, "(ID: " + str(employee1.id) + ")",
      "income tax owing:", employee1.income_taxes())
print(employee2.name, "(ID: " + str(employee2.id) + ")",
      "income tax owing:", employee2.income_taxes(), "\n")

# change employee1 after the fact
employee1.name = "Kevin Minion"
employee1.id = 55555
employee1.income = 1000000

print(employee1.name, "(ID: " + str(employee1.id) + ")",
      "income tax owing:", employee1.income_taxes())
print(employee2.name, "(ID: " + str(employee2.id) + ")",
      "income tax owing:", employee2.income_taxes())
