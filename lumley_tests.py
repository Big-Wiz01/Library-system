# lumley_tests.py
# Simple tests for Lumley Community Library

import lumley_ops as ops

def run_all_tests():
    # Reset environment
    ops.lumley_books.clear()
    ops.lumley_users.clear()

    # --- Test 1: Create book success ---
    assert ops.create_book("T001", "Test Book", "Author A", "Fiction", 3) == \
           "Book created in Lumley Community Library!", "Test 1 Failed"

    # --- Test 2: Create book fail - invalid genre ---
    assert ops.create_book("T002", "Bad Genre", "Author B", "Fantasy", 2) == \
           "Book type not valid! Allowed types: Fiction, Non-Fiction, Sci-Fi", "Test 2 Failed"

    # --- Test 3: Create book fail - invalid copies ---
    assert ops.create_book("T003", "Bad Copies", "Author C", "Non-Fiction", 0) == \
           "Copy number must be at least 1!", "Test 3 Failed"

    # --- Test 4: Create user success ---
    assert ops.create_user(1, "Test User", "test@lumley.sl") == \
           "User created in Lumley Community Library!", "Test 4 Failed"

    # --- Test 5: Lend fail - no available copies ---
    ops.create_book("T004", "Zero Copies", "Author D", "Sci-Fi", 1)
    assert ops.lend_book("T004", 1) == "Book lent successfully from Lumley library!", "Test 5a Failed"
    assert ops.lend_book("T004", 1) == "No copies available to lend!", "Test 5b Failed"
    assert ops.reclaim_book("T004", 1) == "Book reclaimed successfully to Lumley library!", "Test 5c Failed"

    # --- Test 6: Lend success and limit fail ---
    ops.create_book("T005", "B1", "A", "Fiction", 3)
    ops.create_book("T006", "B2", "A", "Fiction", 3)
    ops.create_book("T007", "B3", "A", "Fiction", 3)
    assert ops.lend_book("T005", 1) == "Book lent successfully from Lumley library!"
    assert ops.lend_book("T006", 1) == "Book lent successfully from Lumley library!"
    assert ops.lend_book("T007", 1) == "Book lent successfully from Lumley library!"
    # Try lending a fourth book (should fail)
    ops.create_book("T008", "Extra Book", "A", "Fiction", 2)
    assert ops.lend_book("T008", 1) == "User reached the 3-book lending limit!", "Test 6 Failed"

    # --- Test 7: Return restores available copies ---
    assert ops.reclaim_book("T005", 1) == "Book reclaimed successfully to Lumley library!"
    assert ops.lumley_books["T005"]["available_copies"] == 3, "Test 7 Failed: available copies not restored"

    # --- Test 8: Erase fail when book is lent ---
    # User still has T006 and T007
    assert ops.erase_book("T006") == "Can't erase: Book is currently lent out!", "Test 8 Failed"

    # --- Test 9: Erase success after return ---
    assert ops.reclaim_book("T006", 1) == "Book reclaimed successfully to Lumley library!"
    assert ops.erase_book("T006") == "Book erased from Lumley library!", "Test 9 Failed"

    print("All Lumley tests passed!")

if __name__ == "__main__":
    run_all_tests()
