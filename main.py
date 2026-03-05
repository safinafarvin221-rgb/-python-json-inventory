import json

# Read the inventory
with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total books:", len(inventory))

# New book
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# Add book
inventory.append(new_book)

# Save updated inventory
with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

# Display inventory
for book in inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")