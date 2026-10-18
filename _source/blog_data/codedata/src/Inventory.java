import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Inventory {
    static class Item {
        final String name;
        int qty;
        final double price;

        Item(String name, int qty, double price) {
            this.name = name;
            this.qty = qty;
            this.price = price;
        }

        double value() {
            return qty * price;
        }
    }

    private final Map<String, Item> items = new LinkedHashMap<>();

    public void add(String name, int qty, double price) {
        items.put(name, new Item(name, qty, price));
    }

    public void restock(String name, int amount) {
        items.get(name).qty += amount;
    }

    public boolean sell(String name, int amount) {
        Item item = items.get(name);
        if (item.qty < amount) {
            return false;
        }
        item.qty -= amount;
        return true;
    }

    public List<String> lowStock(int threshold) {
        List<String> names = new ArrayList<>();
        for (Item item : items.values()) {
            if (item.qty <= threshold) {
                names.add(item.name);
            }
        }
        names.sort(null);
        return names;
    }

    public double totalValue() {
        double total = 0;
        for (Item item : items.values()) {
            total += item.value();
        }
        return total;
    }

    public List<String> report() {
        List<Item> rows = new ArrayList<>(items.values());
        rows.sort(Comparator.comparingDouble(Item::value).reversed().thenComparing(item -> item.name));
        List<String> lines = new ArrayList<>();
        for (Item item : rows) {
            lines.add(String.format("%-12s%5d%10.2f", item.name, item.qty, item.value()));
        }
        return lines;
    }

    public static void main(String[] args) {
        Inventory inventory = new Inventory();
        inventory.add("apple", 3, 0.5);
        inventory.add("banana", 12, 0.25);
        inventory.add("cherry", 0, 4.0);
        inventory.add("date", 7, 1.5);
        inventory.add("elderberry", 2, 6.0);
        inventory.restock("cherry", 5);
        System.out.println("Sold banana: " + (inventory.sell("banana", 4) ? "yes" : "no"));
        System.out.println("Sold apple: " + (inventory.sell("apple", 10) ? "yes" : "no"));
        System.out.println("Low stock: " + String.join(", ", inventory.lowStock(3)));
        for (String line : inventory.report()) {
            System.out.println(line);
        }
        System.out.println(String.format("Total: %.2f", inventory.totalValue()));
    }
}
