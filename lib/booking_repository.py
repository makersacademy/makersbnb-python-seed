from lib.booking import Booking

class BookingRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["date"], row["status"], row["space_id"], row["guest_id"])
            bookings.append(item)
        return bookings

    # Find a single book by its id
    def find(self, booking_id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s', [booking_id])
        row = rows[0]
        return Booking(row["id"], row["date"], row["status"], row["space_id"], row["guest_id"])

    # # Create a new book
    # # Do you want to get its id back? Look into RETURNING id;
    # def create(self, book):
    #     self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [
    #                              book.title, book.author_name])
    #     return None

    # # Delete a book by its id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None