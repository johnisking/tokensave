class Item {
  constructor(
    public name: string,
    public qty: number,
    public price: number,
  ) {}

  value(): number {
    return this.qty * this.price;
  }
}

class Inventory {
  private items = new Map<string, Item>();

  add(name: string, qty: number, price: number): void {
    this.items.set(name, new Item(name, qty, price));
  }

  restock(name: string, amount: number): void {
    this.items.get(name)!.qty += amount;
  }

  sell(name: string, amount: number): boolean {
    const item = this.items.get(name)!;
    if (item.qty < amount) {
      return false;
    }
    item.qty -= amount;
    return true;
  }

  lowStock(threshold: number): string[] {
    return [...this.items.values()]
      .filter((item) => item.qty <= threshold)
      .map((item) => item.name)
      .sort();
  }

  totalValue(): number {
    return [...this.items.values()].reduce((sum, item) => sum + item.value(), 0);
  }

  report(): string[] {
    return [...this.items.values()]
      .sort((a, b) => b.value() - a.value() || a.name.localeCompare(b.name))
      .map((item) => item.name.padEnd(12) + String(item.qty).padStart(5) + item.value().toFixed(2).padStart(10));
  }
}

function main(): void {
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
