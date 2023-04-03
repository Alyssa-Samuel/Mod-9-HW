import pandas as pd

class BookLover():
    """The class uses a reader's personal info to organize by favorite, number read, rating, etc."""
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email 
        self.fave_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
         
    def add_book(self, book_name, book_rating):
        """This adds new book to list if the book rating is between 0 and 5 and doesn't exist on the list."""
        self.book_name = str(book_name)
        self.book_rating = int(book_rating)
        
        if book_rating < 0 & book_rating > 5:
            return True
        else: 
            return "The rating is not between 0 and 5."
        
        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]
            })
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
    def has_read(self, book_name):
        """This function returns True if the person read the book or False otherwise."""
        if self.book_name in self.book_list['book_name']:
            return True
        else:
            return False
        
    def num_books_read(self):
        """This function returns total number of books read by person."""
        return self.num_books
        
    def fav_books(self):
        """This function returns person's fav book with a rating higher  than 3."""
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.has_read("War of the Worlds")
    test_object.num_books_read()
    test_object.fav_books()


