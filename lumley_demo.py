# lumley_demo.py
import lumley_ops as ops

# Reset library
ops.lumley_books.clear()
ops.lumley_users.clear()

print("=== Lumley Community Library Demo ===\n")

# Create books
print(ops.create_book("LUM001", "Lumley Local History", "A. Kargbo", "Non-Fiction", 4))
print(ops.create_book("LUM002", "Stories of Sierra Leone", "M. Bangura", "Fiction", 3))
print(ops.create_book("LUM003", "Space Adventures for Kids", "J. Jalloh", "Sci-Fi", 2))
print(ops.create_book("LUM001", "Duplicate Book", "X. X", "Fiction", 1))  # duplicate

# Create users
print("\n-- Users --")
print(ops.create_user(101, "Hannah Conteh", "hannah@lumley.sl"))
print(ops.create_user(102, "Kadiatu Mansaray", "kadiatu@lumley.sl"))
print(ops.create_user(101, "Dup User", "dup@lumley.sl"))  # duplicate

# Borrow books
print("\n-- Borrowing --")
print(ops.lend_book("LUM001", 101))
print(ops.lend_book("LUM002", 101))
print(ops.lend_book("LUM003", 101))
print(ops.lend_book("LUM003", 101))  # already borrowed
print(ops.lend_book("LUM004", 101))  # not found
print(ops.lend_book("LUM001", 999))  # invalid user

# Show library state
print("\n-- Current Library State --")
print("Books:", ops.display_books())
print("Users:", ops.display_users())

# Return and erase
print("\n-- Returning & Deleting --")
print(ops.reclaim_book("LUM002", 101))
print(ops.erase_book("LUM002"))
print(ops.erase_book("LUM004"))  # not found

print("\n=== Demo Complete ===")
