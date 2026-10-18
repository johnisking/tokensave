use std::collections::HashMap;

struct Item {
    name: String,
    qty: u32,
    price: f64,
}

impl Item {
    fn value(&self) -> f64 {
        self.qty as f64 * self.price
    }
}

struct Inventory {
    items: HashMap<String, Item>,
}

impl Inventory {
    fn new() -> Self {
        Inventory { items: HashMap::new() }
    }

    fn add(&mut self, name: &str, qty: u32, price: f64) {
        self.items.insert(name.to_string(), Item { name: name.to_string(), qty, price });
    }

    fn restock(&mut self, name: &str, amount: u32) {
        if let Some(item) = self.items.get_mut(name) {
            item.qty += amount;
        }
    }

    fn sell(&mut self, name: &str, amount: u32) -> bool {
        match self.items.get_mut(name) {
            Some(item) if item.qty >= amount => {
                item.qty -= amount;
                true
            }
            _ => false,
        }
    }

    fn low_stock(&self, threshold: u32) -> Vec<String> {
        let mut names: Vec<String> = self
            .items
            .values()
            .filter(|item| item.qty <= threshold)
            .map(|item| item.name.clone())
            .collect();
        names.sort();
        names
    }

    fn total_value(&self) -> f64 {
        self.items.values().map(|item| item.value()).sum()
    }

    fn report(&self) -> Vec<String> {
        let mut rows: Vec<&Item> = self.items.values().collect();
        rows.sort_by(|a, b| b.value().partial_cmp(&a.value()).unwrap().then_with(|| a.name.cmp(&b.name)));
        rows.iter()
            .map(|item| format!("{:<12}{:>5}{:>10.2}", item.name, item.qty, item.value()))
            .collect()
    }
}

fn yes_no(ok: bool) -> &'static str {
    if ok { "yes" } else { "no" }
}

fn main() {
    let mut inventory = Inventory::new();
    inventory.add("apple", 3, 0.5);
    inventory.add("banana", 12, 0.25);
    inventory.add("cherry", 0, 4.0);
    inventory.add("date", 7, 1.5);
    inventory.add("elderberry", 2, 6.0);
    inventory.restock("cherry", 5);
    println!("Sold banana: {}", yes_no(inventory.sell("banana", 4)));
    println!("Sold apple: {}", yes_no(inventory.sell("apple", 10)));
    println!("Low stock: {}", inventory.low_stock(3).join(", "));
    for line in inventory.report() {
        println!("{}", line);
    }
    println!("Total: {:.2}", inventory.total_value());
}
