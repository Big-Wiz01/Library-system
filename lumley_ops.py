# lumley_ops.py
# Lumley Community Library Management System (Interactive Version)

lumley_books = {}
lumley_users = []
lumley_genres = ('Fiction', 'Non-Fiction', 'Sci-Fi')


def create_book():
    book_code = input("Enter Book Code: ").strip()
    if book_code in lumley_books:
        print("❌ Book code already exists in Lumley library!")
        return

    book_title = input("Enter Book Title: ").strip()
    book_author = input("Enter Author Name: ").strip()
    print(f"Available Book Types: {', '.join(lumley_genres)}")
    book_type = input("Enter Book Type: ").strip()
    if book_type not in lumley_genres:
        print(f"❌ Invalid book type! Allowed types: {', '.join(lumley_genres)}")
        return

    try:
        copy_num = int(input("Enter Number of Copies: "))
        if copy_num < 1:
            print("❌ Copy number must be at least 1!")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    lumley_books[book_code] = {
        "book_title": book_title,
        "book_author": book_author,
        "book_type": book_type,
        "total_copies": copy_num,
        "available_copies": copy_num
    }
    print("✅ Book created in Lumley Community Library!")


def create_user():
    user_id = input("Enter User ID: ").strip()
    if any(u['user_id'] == user_id for u in lumley_users):
        print("❌ User ID already exists!")
        return

    user_name = input("Enter User Name: ").strip()
    user_mail = input("Enter User Email: ").strip()

    lumley_users.append({
        "user_id": user_id,
        "user_name": user_name,
        "user_mail": user_mail,
        "lent_books": []
    })
    print("✅ User created in Lumley Community Library!")


def lend_book():
    book_code = input("Enter Book Code to Lend: ").strip()
    user_id = input("Enter User ID: ").strip()

    if book_code not in lumley_books:
        print("❌ Book code not found in Lumley library!")
        return
    if lumley_books[book_code]['available_copies'] < 1:
        print("❌ No copies available to lend!")
        return

    user = next((u for u in lumley_users if u['user_id'] == user_id), None)
    if not user:
        print("❌ User ID not found in Lumley records!")
        return
    if len(user['lent_books']) >= 3:
        print("❌ User reached the 3-book lending limit!")
        return
    if book_code in user['lent_books']:
        print("❌ User already borrowed this book!")
        return

    user['lent_books'].append(book_code)
    lumley_books[book_code]['available_copies'] -= 1
    print("✅ Book lent successfully from Lumley library!")


def reclaim_book():
    book_code = input("Enter Book Code to Reclaim: ").strip()
    user_id = input("Enter User ID: ").strip()

    if book_code not in lumley_books:
        print("❌ Book code not found in Lumley library!")
        return
    user = next((u for u in lumley_users if u['user_id'] == user_id), None)
    if not user:
        print("❌ User ID not found in Lumley records!")
        return
    if book_code not in user['lent_books']:
        print("❌ This book was not lent to the user!")
        return

    user['lent_books'].remove(book_code)
    lumley_books[book_code]['available_copies'] += 1
    print("✅ Book reclaimed successfully to Lumley library!")


def erase_book():
    book_code = input("Enter Book Code to Erase: ").strip()
    if book_code not in lumley_books:
        print("❌ Book code not found in Lumley library!")
        return
    for u in lumley_users:
        if book_code in u['lent_books']:
            print("❌ Can't erase: Book is currently lent out!")
            return
    del lumley_books[book_code]
    print("✅ Book erased from Lumley library!")


def display_books():
    if not lumley_books:
        print("📚 No books in Lumley Library yet!")
        return
    print("\n📘 Books in Lumley Community Library:")
    for code, info in lumley_books.items():
        print(f"- {code}: {info['book_title']} by {info['book_author']} "
              f"({info['book_type']}) | Available: {info['available_copies']}/{info['total_copies']}")


def display_users():
    if not lumley_users:
        print("👥 No users registered yet!")
        return
    print("\n👤 Users in Lumley Community Library:")
    for u in lumley_users:
        print(f"- {u['user_id']}: {u['user_name']} ({u['user_mail']}) | Borrowed: {u['lent_books']}")


def main():
    while True:
        print("\n=== Lumley Community Library System ===")
        print("1. Add Book")
        print("2. Register User")
        print("3. Lend Book")
        print("4. Reclaim Book")
        print("5. Erase Book")
        print("6. View All Books")
        print("7. View All Users")
        print("8. Exit")
        choice = input("Select an option (1-8): ").strip()

        if choice == '1':
            create_book()
        elif choice == '2':
            create_user()
        elif choice == '3':
            lend_book()
        elif choice == '4':
            reclaim_book()
        elif choice == '5':
            erase_book()
        elif choice == '6':
            display_books()
        elif choice == '7':
            display_users()
        elif choice == '8':
            print("👋 Exiting Lumley Library System. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()