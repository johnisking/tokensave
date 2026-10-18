class Item:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def value(self):
        return self.qty * self.price


class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, name, qty, price):
        self.items[name] = Item(name, qty, price)

    def restock(self, name, amount):
        self.items[name].qty += amount

    def sell(self, name, amount):
        item = self.items[name]
        if item.qty < amount:
            return False
        item.qty -= amount
        return True

    def low_stock(self, threshold):
        return sorted(name for name, item in self.items.items() if item.qty <= threshold)

    def total_value(self):
        return sum(item.value() for item in self.items.values())

    def report(self):
        rows = sorted(self.items.values(), key=lambda item: (-item.value(), item.name))
        return [f"{item.name:<12}{item.qty:>5}{item.value():>10.2f}" for item in rows]


def main():
    inventory = Inventory()
    inventory.add("apple", 3, 0.5)
    inventory.add("banana", 12, 0.25)
    inventory.add("cherry", 0, 4.0)
    inventory.add("date", 7, 1.5)
    inventory.add("elderberry", 2, 6.0)
    inventory.restock("cherry", 5)
    print("Sold banana:", "yes" if inventory.sell("banana", 4) else "no")
    print("Sold apple:", "yes" if inventory.sell("apple", 10) else "no")
    print("Low stock:", ", ".join(inventory.low_stock(3)))
    for line in inventory.report():
        print(line)
    print(f"Total: {inventory.total_value():.2f}")


if __name__ == "__main__":
    main()
