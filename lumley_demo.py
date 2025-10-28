class LumleyLibrary:
    def __init__(self):
        self.books = {}
        self.users = []

    # ---------- BOOK SECTION ----------
    def create_book(self, code, title, author, book_type, copies):
        if code in self.books:
            print("Book code already exists in Lumley library!")
        else:
            self.books[code] = {
                "book_title": title,
                "book_author": author,
                "book_type": book_type,
                "total_copies": copies,
                "available_copies": copies
            }
            print(f"✅ Book created in Lumley Community Library: {title} by {author} ({book_type})")

    # ---------- USER SECTION ----------
    def create_user(self, user_id, name, mail):
        for user in self.users:
            if user["user_id"] == user_id:
                print("❌ User ID already in system!")
                return
        self.users.append({
            "user_id": user_id,
            "user_name": name,
            "user_mail": mail,
            "lent_books": []
        })
        print(f"✅ User created in Lumley Community Library: {name} ({mail})")

    # ---------- BORROW SECTION ----------
    def lend_book(self, code, user_id):
        user = next((u for u in self.users if u["user_id"] == user_id), None)
        if not user:
            print("❌ User ID not found in Lumley records!")
            return
        if code not in self.books:
            print("❌ Book code not found in Lumley library!")
            return
        if len(user["lent_books"]) >= 3:
            print("⚠️ User reached the 3-book lending limit!")
            return
        book = self.books[code]
        if book["available_copies"] > 0:
            book["available_copies"] -= 1
            user["lent_books"].append(code)
            print(f"📘 Book lent successfully: {code} → {user['user_name']}")
        else:
            print("⚠️ No copies available to lend!")

    # ---------- RETURN SECTION ----------
    def return_book(self, code, user_id):
        user = next((u for u in self.users if u["user_id"] == user_id), None)
        if not user:
            print("❌ User ID not found in Lumley records!")
            return
        if code not in user["lent_books"]:
            print("⚠️ This user didn’t borrow that book!")
            return
        user["lent_books"].remove(code)
        if code in self.books:
            self.books[code]["available_copies"] += 1
            print(f"✅ Book reclaimed successfully: {code} from {user['user_name']}")
        else:
            print("⚠️ Book not found in system records!")

    # ---------- DELETE SECTION ----------
    def delete_book(self, code):
        if code in self.books:
            del self.books[code]
            print(f"🗑️ Book erased from Lumley library: {code}")
        else:
            print("❌ Book code not found in Lumley library!")

# ---------------- DEMO RUN ----------------
def run_demo():
    print("=== Lumley Community Library Demo ===\n")

    lumley = LumleyLibrary()

    # Books
    lumley.create_book("LUM001", "Lumley Local History", "A. Kargbo", "Non-Fiction", 4)
    lumley.create_book("LUM002", "Stories of Sierra Leone", "M. Bangura", "Fiction", 3)
    lumley.create_book("LUM003", "Space Adventures for Kids", "J. Jalloh", "Sci-Fi", 2)
    lumley.create_book("LUM001", "Duplicate Test", "A. Koroma", "Drama", 1)

    print("\n-- Users --")
    lumley.create_user(101, "Hannah Conteh", "hannah@lumley.sl")
    lumley.create_user(102, "Kadiatu Mansaray", "kadiatu@lumley.sl")
    lumley.create_user(101, "Duplicate User", "dup@lumley.sl")

    print("\n-- Borrowing --")
    lumley.lend_book("LUM001", 101)
    lumley.lend_book("LUM002", 101)
    lumley.lend_book("LUM003", 101)
    lumley.lend_book("LUM002", 101)  # limit test
    lumley.lend_book("LUM999", 101)  # invalid book
    lumley.lend_book("LUM001", 999)  # invalid user

    print("\n-- Current Library State --")
    print("Books:", lumley.books)
    print("Users:", lumley.users)

    print("\n-- Returning & Deleting --")
    lumley.return_book("LUM002", 101)
    lumley.delete_book("LUM002")
    lumley.delete_book("LUM999")

    print("\n=== Demo Complete ===")

# Make sure the demo runs
if __name__ == "__main__":
    run_demo()


