# lumley_ops.py
# Lumley Community Library Management System

# Use lumley_books and lumley_users everywhere
lumley_books = {}
lumley_users = []
lumley_genres = ('Fiction', 'Non-Fiction', 'Sci-Fi')


def create_book(book_code, book_title, book_author, book_type, copy_num):
    if book_code in lumley_books:
        return "Book code already exists in Lumley library!"
    if book_type not in lumley_genres:
        return f"Book type not valid! Allowed types: {', '.join(lumley_genres)}"
    if copy_num < 1:
        return "Copy number must be at least 1!"
    lumley_books[book_code] = {
        "book_title": book_title,
        "book_author": book_author,
        "book_type": book_type,
        "total_copies": copy_num,
        "available_copies": copy_num
    }
    return "Book created in Lumley Community Library!"


def create_user(user_id, user_name, user_mail):
    if any(u['user_id'] == user_id for u in lumley_users):
        return "User ID already in system!"
    lumley_users.append({
        "user_id": user_id,
        "user_name": user_name,
        "user_mail": user_mail,
        "lent_books": []
    })
    return "User created in Lumley Community Library!"


def lend_book(book_code, user_id):
    if book_code not in lumley_books:
        return "Book code not found in Lumley library!"
    if lumley_books[book_code]['available_copies'] < 1:
        return "No copies available to lend!"
    user = next((u for u in lumley_users if u['user_id'] == user_id), None)
    if not user:
        return "User ID not found in Lumley records!"
    if len(user['lent_books']) >= 3:
        return "User reached the 3-book lending limit!"
    if book_code in user['lent_books']:
        return "User already borrowed this book!"
    user['lent_books'].append(book_code)
    lumley_books[book_code]['available_copies'] -= 1
    return "Book lent successfully from Lumley library!"


def reclaim_book(book_code, user_id):
    if book_code not in lumley_books:
        return "Book code not found in Lumley library!"
    user = next((u for u in lumley_users if u['user_id'] == user_id), None)
    if not user:
        return "User ID not found in Lumley records!"
    if book_code not in user['lent_books']:
        return "This book was not lent to the user!"
    user['lent_books'].remove(book_code)
    lumley_books[book_code]['available_copies'] += 1
    return "Book reclaimed successfully to Lumley library!"


def erase_book(book_code):
    if book_code not in lumley_books:
        return "Book code not found in Lumley library!"
    for u in lumley_users:
        if book_code in u['lent_books']:
            return "Can't erase: Book is currently lent out!"
    del lumley_books[book_code]
    return "Book erased from Lumley library!"


def display_books():
    return lumley_books


def display_users():
    return lumley_users
