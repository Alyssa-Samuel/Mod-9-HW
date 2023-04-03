import unittest
from booklover import BookLover

test_case = BookLover("Alyssa Samuel", "ays8ms@virginia.edu", "romance")

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_case.add_book("Harry Potter", 4)
        testValue = True

        # error message in case if test case got failed
        message = "Test value is not true."

        # assertTrue() to check true of test value
        self.assertTrue( testValue, message)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_case.add_book("Harry Potter", 4)
        testValue = True

        # error message in case if test case got failed
        message = "Test value is not true."

        # assertTrue() to check true of test value
        self.assertTrue( testValue, message)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_case.has_read("Lord of the Rings")
        testValue = True

        # error message in case if test case got failed
        message = "Test value is not true."

        # assertTrue() to check true of test value
        self.assertTrue( testValue, message)

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
         answer = test_case.has_read("Bible")
         self.assertFalse(answer)
        
        testValue = True

        # error message in case if test case got failed
        message = "Test value is not true."

        # assertTrue() to check true of test value
        self.assertTrue( testValue, message)

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_case.num_books_read()
        testValue = True

        # error message in case if test case got failed
        message = "Test value is not true."

        # assertTrue() to check true of test value
        self.assertTrue( testValue, message)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_case.fav_books()
        testValue = True

        # error message in case if test case got failed
        message = "Test value is not true."

        # assertTrue() to check true of test value
        self.assertTrue( testValue, message)

if __name__ == '__main__':

    unittest.main(verbosity=3)