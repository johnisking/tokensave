<?php

class Item
{
    public function __construct(
        public string $name,
        public int $qty,
        public float $price,
    ) {
    }

    public function value(): float
    {
        return $this->qty * $this->price;
    }
}

class Inventory
{
    private array $items = [];

    public function add(string $name, int $qty, float $price): void
    {
        $this->items[$name] = new Item($name, $qty, $price);
    }

    public function restock(string $name, int $amount): void
    {
        $this->items[$name]->qty += $amount;
    }

    public function sell(string $name, int $amount): bool
    {
        $item = $this->items[$name];
        if ($item->qty < $amount) {
            return false;
        }
        $item->qty -= $amount;
        return true;
    }

    public function lowStock(int $threshold): array
    {
        $names = [];
        foreach ($this->items as $item) {
            if ($item->qty <= $threshold) {
                $names[] = $item->name;
            }
        }
        sort($names);
        return $names;
    }

    public function totalValue(): float
    {
        return array_sum(array_map(fn (Item $item) => $item->value(), $this->items));
    }

    public function report(): array
    {
        $rows = array_values($this->items);
        usort($rows, fn (Item $a, Item $b) => [$b->value(), $a->name] <=> [$a->value(), $b->name]);
        return array_map(fn (Item $item) => sprintf('%-12s%5d%10.2f', $item->name, $item->qty, $item->value()), $rows);
    }
}

$inventory = new Inventory();
$inventory->add('apple', 3, 0.5);
$inventory->add('banana', 12, 0.25);
$inventory->add('cherry', 0, 4.0);
$inventory->add('date', 7, 1.5);
$inventory->add('elderberry', 2, 6.0);
$inventory->restock('cherry', 5);
echo 'Sold banana: ' . ($inventory->sell('banana', 4) ? 'yes' : 'no') . "\n";
echo 'Sold apple: ' . ($inventory->sell('apple', 10) ? 'yes' : 'no') . "\n";
echo 'Low stock: ' . implode(', ', $inventory->lowStock(3)) . "\n";
foreach ($inventory->report() as $line) {
    echo $line . "\n";
}
printf("Total: %.2f\n", $inventory->totalValue());
