from lib.booking import Booking
from datetime import timedelta

class BookingRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            bookings.append(Booking(row["id"], row["start_date"], row["end_date"], row["property_id"], row["user_id"]))
        return  bookings

    def find(self, id):
        row = self.connection.execute('SELECT * FROM bookings WHERE id=%s', [id])
        row = row[0]
        return Booking(row["id"], row["start_date"], row["end_date"], row["property_id"], row["user_id"])


    def create(self,booking):
        row = self.connection.execute('INSERT INTO bookings(start_date, end_date, property_id, user_id) VALUES (%s,%s,%s,%s) RETURNING id',[
            booking.start_date, booking.end_date, booking.property_id, booking.user_id])
        booking.id = row[0]["id"]
        return booking
    
    def find_by_property_id(self, property_id):
        rows = self.connection.execute('SELECT * FROM bookings WHERE property_id=%s', [property_id])
        bookings_for_property_id = []
        for row in rows:
            bookings_for_property_id.append(Booking(row['id'], row["start_date"], row["end_date"], row["property_id"], row["user_id"]))
        return bookings_for_property_id
    
    def date_range_maker(self, start_date, end_date):
        dates = []
        delta = timedelta(days=1)
        
        while start_date <= end_date:
            dates.append(start_date)
            start_date += delta
        return dates
    
    def availability_checker(self, booking_to_check):
        bookings = self.find_by_property_id(booking_to_check.property_id)
        booked_dates = []
        for booking in bookings:
            booked_dates.extend(self.date_range_maker(booking.start_date, booking.end_date))
        print("Dates already booked")
        print(booked_dates)
        dates_to_check = self.date_range_maker(booking_to_check.start_date, booking_to_check.end_date)
        print("Dates to check")
        print(dates_to_check)
        for date in dates_to_check:
            if date in booked_dates:
                print("!!!!")
                return False
        return True
                

        # for booking in bookings:
        #     date_ranges[booking.start_date] = booking.end_date
        # for item in date_ranges.items():
        #     start_date = item[0]
        #     end_date = item[1]
        #     delta = timedelta(days=1)
        #     while start_date <= end_date:
        #         already_booked_dates.append(start_date)
        #         start_date += delta
        # if booking_to_check.start_date in dates or booking_to_check.end_date in dates:
        #     return False
        # else:
        #     return True
            









    