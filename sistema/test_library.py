import unittest
from datetime import date, timedelta
import library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        library.seed_sample_data()

    def test_seed_books_and_users(self):
        self.assertEqual(len(library.users), 2)
        self.assertEqual(len(library.books), 5)

    def test_search_books_by_title(self):
        res = library.search_books("harry")
        self.assertTrue(any("Harry Potter" in b['title'] for b in res))

    def test_borrow_and_return_no_fine(self):
        user = library.get_user(1)
        hp = next(b for b in library.books if "Harry Potter" in b['title'])
        loan = library.borrow_book(user['id'], hp['id'], days=1)
        self.assertIsNotNone(loan)
        
        fine = library.return_book(loan['loan_id'], return_date=date.today() + timedelta(days=1))
        self.assertEqual(fine, 0.0)
        self.assertEqual(library.get_book(hp['id'])['copies_available'], hp['copies_total'])

    def test_borrow_when_unavailable(self):
        hobbit = next(b for b in library.books if b['title']=="O Hobbit")
        u1 = library.get_user(1)
        u2 = library.get_user(2)
        loan1 = library.borrow_book(u1['id'], hobbit['id'])
        self.assertIsNotNone(loan1)
        loan2 = library.borrow_book(u2['id'], hobbit['id'])
        self.assertIsNone(loan2)  

    def test_return_with_fine_and_payment(self):
        user = library.get_user(1)
        book = next(b for b in library.books if "Jogos Vorazes" in b['title'])
        loan = library.borrow_book(user['id'], book['id'], days=1)
        
        overdue_return = date.today() + timedelta(days=4)
        fine = library.return_book(loan['loan_id'], return_date=overdue_return)
        self.assertEqual(fine, 3.0)  
        self.assertEqual(user['fines'], 3.0)
        paid = library.pay_fine(user['id'], 2.0)
        self.assertEqual(paid, 2.0)
        self.assertEqual(user['fines'], 1.0)

if __name__ == "__main__":
    unittest.main()

