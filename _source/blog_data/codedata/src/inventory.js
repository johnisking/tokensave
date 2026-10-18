class Item {
  constructor(name, qty, price) {
    this.name = name;
    this.qty = qty;
    this.price = price;
  }

  value() {
    return this.qty * this.price;
  }
}

class Inventory {
  constructor() {
    this.items = new Map();
  }

  add(name, qty, price) {
    this.items.set(name, new Item(name, qty, price));
  }

  restock(name, amount) {
    this.items.get(name).qty += amount;
  }

  sell(name, amount) {
    const item = this.items.get(name);
    if (item.qty < amount) {
      return false;
    }
    item.qty -= amount;
    return true;
  }

  lowStock(threshold) {
    return [...this.items.values()]
      .filter((item) => item.qty <= threshold)
      .map((item) => item.name)
      .sort();
  }

  totalValue() {
    return [...this.items.values()].reduce((sum, item) => sum + item.value(), 0);
  }

  report() {
    return [...this.items.values()]
      .sort((a, b) => b.value() - a.value() || a.name.localeCompare(b.name))
      .map((item) => item.name.padEnd(12) + String(item.qty).padStart(5) + item.value().toFixed(2).padStart(10));
  }
}

function main() {
  const inventory = new Inventory();
  inventory.add("apple", 3, 0.5);
  inventory.add("banana", 12, 0.25);
  inventory.add("cherry", 0, 4.0);
  inventory.add("date", 7, 1.5);
  inventory.add("elderberry", 2, 6.0);
  inventory.restock("cherry", 5);
  console.log("Sold banana:", inventory.sell("banana", 4) ? "yes" : "no");
  console.log("Sold apple:", inventory.sell("apple", 10) ? "yes" : "no");
  console.log("Low stock:", inventory.lowStock(3).join(", "));
  for (const line of inventory.report()) {
    console.log(line);
  }
  console.log(`Total: ${inventory.totalValue().toFixed(2)}`);
}

main();
