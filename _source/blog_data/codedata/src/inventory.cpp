#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <vector>

struct Item {
    std::string name;
    int qty;
    double price;

    double value() const { return qty * price; }
};

class Inventory {
public:
    void add(const std::string& name, int qty, double price) {
        items_[name] = Item{name, qty, price};
    }

    void restock(const std::string& name, int amount) {
        items_[name].qty += amount;
    }

    bool sell(const std::string& name, int amount) {
        Item& item = items_[name];
        if (item.qty < amount) {
            return false;
        }
        item.qty -= amount;
        return true;
    }

    std::vector<std::string> lowStock(int threshold) const {
        std::vector<std::string> names;
        for (const auto& [name, item] : items_) {
            if (item.qty <= threshold) {
                names.push_back(name);
            }
        }
        return names;
    }

    double totalValue() const {
        double total = 0;
        for (const auto& [name, item] : items_) {
            total += item.value();
        }
        return total;
    }

    std::vector<std::string> report() const {
        std::vector<Item> rows;
        for (const auto& [name, item] : items_) {
            rows.push_back(item);
        }
        std::sort(rows.begin(), rows.end(), [](const Item& a, const Item& b) {
            if (a.value() != b.value()) {
                return a.value() > b.value();
            }
            return a.name < b.name;
        });
        std::vector<std::string> lines;
        for (const Item& item : rows) {
            char buffer[64];
            std::snprintf(buffer, sizeof(buffer), "%-12s%5d%10.2f", item.name.c_str(), item.qty, item.value());
            lines.push_back(buffer);
        }
        return lines;
    }

private:
    std::map<std::string, Item> items_;
};

std::string join(const std::vector<std::string>& parts, const std::string& sep) {
    std::string result;
    for (size_t i = 0; i < parts.size(); ++i) {
        if (i > 0) {
            result += sep;
        }
        result += parts[i];
    }
    return result;
}

int main() {
    Inventory inventory;
    inventory.add("apple", 3, 0.5);
    inventory.add("banana", 12, 0.25);
    inventory.add("cherry", 0, 4.0);
    inventory.add("date", 7, 1.5);
    inventory.add("elderberry", 2, 6.0);
    inventory.restock("cherry", 5);
    std::cout << "Sold banana: " << (inventory.sell("banana", 4) ? "yes" : "no") << "\n";
    std::cout << "Sold apple: " << (inventory.sell("apple", 10) ? "yes" : "no") << "\n";
    std::cout << "Low stock: " << join(inventory.lowStock(3), ", ") << "\n";
    for (const std::string& line : inventory.report()) {
        std::cout << line << "\n";
    }
    std::printf("Total: %.2f\n", inventory.totalValue());
    return 0;
}
