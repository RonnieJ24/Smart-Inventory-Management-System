class Product:
    def __init__(self, id, name, category, price, stock):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"{self.name} (ID: {self.id}, Price: {self.price}, Stock: {self.stock})"


class Inventory:
    def __init__(self):
        self.products = {}  # Hash table for storing products

    def add_product(self, product):
        self.products[product.id] = product

    def lookup_product(self, product_id):
        return self.products.get(product_id, "Product not found")

    def quicksort(self, attribute):
        products_list = list(self.products.values())

        def sort(products):
            if len(products) <= 1:
                return products
            else:
                pivot = getattr(products[0], attribute)
                lesser = [
                    product
                    for product in products[1:]
                    if getattr(product, attribute) <= pivot
                ]
                greater = [
                    product
                    for product in products[1:]
                    if getattr(product, attribute) > pivot
                ]
                return sort(lesser) + [products[0]] + sort(greater)

        return sort(products_list)


class WarehouseGraph:
    def __init__(self):
        self.paths = {}  # Graph representing the warehouse layout

    def add_path(self, start, end, distance):
        if start not in self.paths:
            self.paths[start] = {}
        self.paths[start][end] = distance

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.paths:
            return None
        shortest_path = None
        for node in self.paths[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest_path or len(newpath) < len(shortest_path):
                        shortest_path = newpath
        return shortest_path


# Simplified Binary Search Tree as a placeholder for RB-Tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Simplified insert method for demonstration
    def insert(self, value):
        # Placeholder for the actual insert logic
        pass

    # Simplified search method for demonstration
    def search(self, value):
        # Placeholder for the actual search logic
        pass


# Efficiency Analysis Function
def analyze_efficiency(func, *args):
    import time

    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Time taken for {func.__name__}: {end_time - start_time} seconds")
    return result


# Example Usage
inventory = Inventory()
inventory.add_product(Product(101, "Smartphone", "Electronics", 999.99, 50))
inventory.add_product(Product(102, "Laptop", "Electronics", 1200.00, 30))

# Lookup and Sorting with Efficiency Analysis
print(
    analyze_efficiency(inventory.lookup_product, 101)
)  # Hash Table Lookup with analysis
print(
    "Sorted by Price:", analyze_efficiency(inventory.quicksort, "price")
)  # Quicksort with analysis

# Warehouse Graph
warehouse = WarehouseGraph()
warehouse.add_path("Entrance", "Aisle1", 5)
warehouse.add_path("Aisle1", "Aisle2", 10)
warehouse.add_path("Aisle1", "Checkout", 15)
warehouse.add_path("Aisle2", "Checkout", 5)
print(
    "Shortest Path from Entrance to Checkout:",
    analyze_efficiency(warehouse.find_shortest_path, "Entrance", "Checkout"),
)

# Binary Search Tree Usage (Placeholder for RB-Tree)
bst = BinarySearchTree()
# bst.insert() logic would be used here
# bst.search() logic would be used here
