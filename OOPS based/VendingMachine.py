class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self):
        self.items = []
        self.balance = 0

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item.name} - ${item.price:.2f}")

    def insert_coin(self, amount):
        self.balance += amount

    def purchase_item(self, item_idx):
        if 1 <= item_idx <= len(self.items):
            selected_item = self.items[item_idx - 1]
            if self.balance >= selected_item.price:
                print(f"Purchased {selected_item.name} for ${selected_item.price:.2f}")
                self.balance -= selected_item.price
                del self.items[item_idx - 1]
            else:
                print("Insufficient balance.")
        else:
            print("Invalid item index.")

    def get_balance(self):
        return self.balance

item1 = Item("Soda", 1.50)
item2 = Item("Chips", 1.00)
item3 = Item("Candy", 0.75)

vending_machine = VendingMachine()

vending_machine.add_item(item1)
vending_machine.add_item(item2)
vending_machine.add_item(item3)

vending_machine.display_items()

vending_machine.insert_coin(2.00)

vending_machine.purchase_item(1)
vending_machine.purchase_item(2)

print("Remaining balance:", vending_machine.get_balance())
