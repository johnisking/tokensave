#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ITEMS 16

typedef struct {
    char name[32];
    int qty;
    double price;
} Item;

typedef struct {
    Item items[MAX_ITEMS];
    int count;
} Inventory;

static double item_value(const Item *item) {
    return item->qty * item->price;
}

static Item *find_item(Inventory *inv, const char *name) {
    for (int i = 0; i < inv->count; i++) {
        if (strcmp(inv->items[i].name, name) == 0) {
            return &inv->items[i];
        }
    }
    return NULL;
}

static void add_item(Inventory *inv, const char *name, int qty, double price) {
    Item *item = &inv->items[inv->count++];
    strncpy(item->name, name, sizeof(item->name) - 1);
    item->name[sizeof(item->name) - 1] = '\0';
    item->qty = qty;
    item->price = price;
}

static void restock(Inventory *inv, const char *name, int amount) {
    find_item(inv, name)->qty += amount;
}

static bool sell(Inventory *inv, const char *name, int amount) {
    Item *item = find_item(inv, name);
    if (item->qty < amount) {
        return false;
    }
    item->qty -= amount;
    return true;
}

static int compare_names(const void *a, const void *b) {
    return strcmp(*(const char *const *)a, *(const char *const *)b);
}

static void print_low_stock(const Inventory *inv, int threshold) {
    const char *names[MAX_ITEMS];
    int n = 0;
    for (int i = 0; i < inv->count; i++) {
        if (inv->items[i].qty <= threshold) {
            names[n++] = inv->items[i].name;
        }
    }
    qsort(names, n, sizeof(names[0]), compare_names);
    printf("Low stock: ");
    for (int i = 0; i < n; i++) {
        printf("%s%s", i > 0 ? ", " : "", names[i]);
    }
    printf("\n");
}

static double total_value(const Inventory *inv) {
    double total = 0;
    for (int i = 0; i < inv->count; i++) {
        total += item_value(&inv->items[i]);
    }
    return total;
}

static int compare_items(const void *a, const void *b) {
    const Item *x = a;
    const Item *y = b;
    double vx = item_value(x);
    double vy = item_value(y);
    if (vx != vy) {
        return vx < vy ? 1 : -1;
    }
    return strcmp(x->name, y->name);
}

static void print_report(const Inventory *inv) {
    Item rows[MAX_ITEMS];
    memcpy(rows, inv->items, sizeof(Item) * inv->count);
    qsort(rows, inv->count, sizeof(Item), compare_items);
    for (int i = 0; i < inv->count; i++) {
        printf("%-12s%5d%10.2f\n", rows[i].name, rows[i].qty, item_value(&rows[i]));
    }
}

int main(void) {
    Inventory inventory = {.count = 0};
    add_item(&inventory, "apple", 3, 0.5);
    add_item(&inventory, "banana", 12, 0.25);
    add_item(&inventory, "cherry", 0, 4.0);
    add_item(&inventory, "date", 7, 1.5);
    add_item(&inventory, "elderberry", 2, 6.0);
    restock(&inventory, "cherry", 5);
    printf("Sold banana: %s\n", sell(&inventory, "banana", 4) ? "yes" : "no");
    printf("Sold apple: %s\n", sell(&inventory, "apple", 10) ? "yes" : "no");
    print_low_stock(&inventory, 3);
    print_report(&inventory);
    printf("Total: %.2f\n", total_value(&inventory));
    return 0;
}
