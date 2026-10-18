class Item
  attr_reader :name, :price
  attr_accessor :qty

  def initialize(name, qty, price)
    @name = name
    @qty = qty
    @price = price
  end

  def value
    qty * price
  end
end

class Inventory
  def initialize
    @items = {}
  end

  def add(name, qty, price)
    @items[name] = Item.new(name, qty, price)
  end

  def restock(name, amount)
    @items[name].qty += amount
  end

  def sell(name, amount)
    item = @items[name]
    return false if item.qty < amount

    item.qty -= amount
    true
  end

  def low_stock(threshold)
    @items.values.select { |item| item.qty <= threshold }.map(&:name).sort
  end

  def total_value
    @items.values.sum(&:value)
  end

  def report
    @items.values
          .sort_by { |item| [-item.value, item.name] }
          .map { |item| format('%-12s%5d%10.2f', item.name, item.qty, item.value) }
  end
end

inventory = Inventory.new
inventory.add('apple', 3, 0.5)
inventory.add('banana', 12, 0.25)
inventory.add('cherry', 0, 4.0)
inventory.add('date', 7, 1.5)
inventory.add('elderberry', 2, 6.0)
inventory.restock('cherry', 5)
puts "Sold banana: #{inventory.sell('banana', 4) ? 'yes' : 'no'}"
puts "Sold apple: #{inventory.sell('apple', 10) ? 'yes' : 'no'}"
puts "Low stock: #{inventory.low_stock(3).join(', ')}"
inventory.report.each { |line| puts line }
puts format('Total: %.2f', inventory.total_value)
