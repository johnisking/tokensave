package main

import (
	"fmt"
	"sort"
	"strings"
)

type Item struct {
	Name  string
	Qty   int
	Price float64
}

func (i *Item) Value() float64 {
	return float64(i.Qty) * i.Price
}

type Inventory struct {
	items map[string]*Item
}

func NewInventory() *Inventory {
	return &Inventory{items: make(map[string]*Item)}
}

func (inv *Inventory) Add(name string, qty int, price float64) {
	inv.items[name] = &Item{Name: name, Qty: qty, Price: price}
}

func (inv *Inventory) Restock(name string, amount int) {
	inv.items[name].Qty += amount
}

func (inv *Inventory) Sell(name string, amount int) bool {
	item := inv.items[name]
	if item.Qty < amount {
		return false
	}
	item.Qty -= amount
	return true
}

func (inv *Inventory) LowStock(threshold int) []string {
	var names []string
	for _, item := range inv.items {
		if item.Qty <= threshold {
			names = append(names, item.Name)
		}
	}
	sort.Strings(names)
	return names
}

func (inv *Inventory) TotalValue() float64 {
	total := 0.0
	for _, item := range inv.items {
		total += item.Value()
	}
	return total
}

func (inv *Inventory) Report() []string {
	rows := make([]*Item, 0, len(inv.items))
	for _, item := range inv.items {
		rows = append(rows, item)
	}
	sort.Slice(rows, func(a, b int) bool {
		if rows[a].Value() != rows[b].Value() {
			return rows[a].Value() > rows[b].Value()
		}
		return rows[a].Name < rows[b].Name
	})
	lines := make([]string, 0, len(rows))
	for _, item := range rows {
		lines = append(lines, fmt.Sprintf("%-12s%5d%10.2f", item.Name, item.Qty, item.Value()))
	}
	return lines
}

func yesNo(ok bool) string {
	if ok {
		return "yes"
	}
	return "no"
}

func main() {
	inventory := NewInventory()
	inventory.Add("apple", 3, 0.5)
	inventory.Add("banana", 12, 0.25)
	inventory.Add("cherry", 0, 4.0)
	inventory.Add("date", 7, 1.5)
	inventory.Add("elderberry", 2, 6.0)
	inventory.Restock("cherry", 5)
	fmt.Println("Sold banana:", yesNo(inventory.Sell("banana", 4)))
	fmt.Println("Sold apple:", yesNo(inventory.Sell("apple", 10)))
	fmt.Println("Low stock:", strings.Join(inventory.LowStock(3), ", "))
	for _, line := range inventory.Report() {
		fmt.Println(line)
	}
	fmt.Printf("Total: %.2f\n", inventory.TotalValue())
}
