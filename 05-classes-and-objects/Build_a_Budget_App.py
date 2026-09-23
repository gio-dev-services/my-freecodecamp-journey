class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.__account_funds = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        if amount > 0:
            self.__account_funds += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.__account_funds -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__account_funds

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.__account_funds:
            return False
        else:
            return True

    def __str__(self):
        lines = [self.name.center(30, "*")]

        for entry in self.ledger:
            description = entry["description"][:23]
            amount = entry["amount"]
            lines.append(f"{description:<23}{amount:>7.2f}")

        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    if not categories:
        return "Percentage spent by category"

    expenses = []
    total = 0
    for category in categories:
        spent = sum(-entry["amount"] for entry in category.ledger if entry["amount"] < 0)
        expenses.append(spent)
        total += spent

    percentages = []
    for expense in expenses:
        if total == 0:
            percentages.append(0)
        else:
            percentages.append(int(expense / total * 100) // 10 * 10)

    lines = ["Percentage spent by category"]

    for i in range(100, -1, -10):
        line = f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                line += "o  "
            else:
                line += "   "
        lines.append(line)

    lines.append("    " + "---" * len(categories) + "-")

    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        line = "     "
        for name in names:
            line += (name[i] if i < len(name) else " ") + "  "
        lines.append(line)

    return "\n".join(lines)


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print()

print(create_spend_chart([food, clothing]))
