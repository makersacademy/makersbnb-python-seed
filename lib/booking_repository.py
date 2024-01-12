from lib.booking import Booking
from datetime import date
import requests
from dotenv import load_dotenv
import os

load_dotenv()


class BookingRepository:
    global_mobilenum = os.getenv("MOBILE_NUMBER")
    # Enter users mobile number in format +449999999999

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            """
            SELECT * FROM bookings;
            """
        )
        bookings = []
        for row in rows:
            if row["confirmed"] == "1":
                confirmed = True
            elif row["confirmed"] == "0":
                confirmed = False
            else:
                confirmed = None
            bookings.append(
                Booking(
                    row["id"], row["date"], row["space_id"], row["guest_id"], confirmed
                )
            )
        return bookings

    def find(self, id):
        if id in [booking.id for booking in self.all()]:
            row = self._connection.execute(
                """
                SELECT * FROM bookings WHERE id=%s;
                """,
                [id],
            )[0]
            if row["confirmed"] == "1":
                confirmed = True
            elif row["confirmed"] == "0":
                confirmed = False
            else:
                confirmed = None
            return Booking(
                row["id"], row["date"], row["space_id"], row["guest_id"], confirmed
            )
        else:
            raise Exception("Booking does not exist.")

    def find_by_guest_id(self, guest_id):
        if guest_id in [booking.guest_id for booking in self.all()]:
            rows = self._connection.execute(
                """
                SELECT * FROM bookings WHERE guest_id=%s;
                """,
                [guest_id],
            )
            bookings = []
            for row in rows:
                if row["confirmed"] == "1":
                    confirmed = True
                elif row["confirmed"] == "0":
                    confirmed = False
                else:
                    confirmed = None
                bookings.append(
                    Booking(
                        row["id"],
                        row["date"],
                        row["space_id"],
                        row["guest_id"],
                        confirmed,
                    )
                )
            return bookings
        else:
            return []

    def find_by_space_id(self, space_id):
        if space_id in [booking.space_id for booking in self.all()]:
            rows = self._connection.execute(
                """
                SELECT * FROM bookings WHERE space_id=%s;
                """,
                [space_id],
            )
            bookings = []
            for row in rows:
                if row["confirmed"] == "1":
                    confirmed = True
                elif row["confirmed"] == "0":
                    confirmed = False
                else:
                    confirmed = None
                bookings.append(
                    Booking(
                        row["id"],
                        row["date"],
                        row["space_id"],
                        row["guest_id"],
                        confirmed,
                    )
                )
            return bookings
        else:
            return []

    def create(self, booking):
        date = booking.date
        space_id = booking.space_id
        guest_id = booking.guest_id
        if confirmed := booking.confirmed:
            confirmed = "1"
        elif confirmed == False:
            confirmed = "0"
        else:
            confirmed = None
        # Check that the space is listed for the requested date.
        date_rows = self._connection.execute(
            """
            SELECT * FROM dates where date=%s AND space_id=%s;
            """,
            [date.isoformat(), space_id],
        )
        if len(date_rows) > 0:
            # Check if this booking has been made before.
            guest_bookings = self.find_by_guest_id(guest_id)
            if (str(date), str(space_id)) in [(str(booking.date), str(booking.space_id))
                                    for booking
                                    in guest_bookings]:
                raise Exception("You have already made a booking request for this space on that date!")
            self._connection.execute(
                """
                INSERT INTO bookings (date, space_id, guest_id, confirmed) VALUES (%s, %s, %s, %s);
                """,
                [date.isoformat(), space_id, booking.guest_id, confirmed],
            )
            if self.global_mobilenum != "":
                self.send_sms("Booking confirm", self.global_mobilenum)
        else:
            raise Exception("That date is not available!")
        return None

    def delete(self, id):
        if id in [booking.id for booking in self.all()]:
            self._connection.execute(
                """
                DELETE FROM bookings WHERE id=%s;
                """,
                [id],
            )
            return None
        else:
            raise Exception("Booking does not exist.")

    def update(self, booking):
        if booking.id not in [booking.id for booking in self.all()]:
            raise Exception("Booking does not exist.")
        if confirmed := booking.confirmed:
            confirmed = "1"
        elif confirmed == False:
            confirmed = "0"
        else:
            confirmed = None
        self._connection.execute(
            """
            UPDATE bookings
            SET date=%s, space_id=%s, guest_id=%s, confirmed=%s
            WHERE id=%s;
            """,
            [
                booking.date.isoformat(),
                booking.space_id,
                booking.guest_id,
                confirmed,
                booking.id,
            ],
        )
        return None

    def confirm(self, booking_id):
        if booking_id in [booking.id for booking in self.all()]:
            booking = self.find(booking_id)
            booking.confirmed = True
            self.update(booking)
            self._connection.execute(
                """
                DELETE FROM dates WHERE date=%s AND space_id=%s;
                """,
                [booking.date.isoformat(), booking.space_id],
            )
            if self.global_mobilenum != "":
                self.send_sms("Booking confirm", self.global_mobilenum)
            return True
        else:
            raise Exception("Booking does not exist.")

    def reject(self, booking_id):
        if booking_id in [booking.id for booking in self.all()]:
            booking = self.find(booking_id)
            booking.confirmed = False
            self.update(booking)
            if self.global_mobilenum != "":
                self.send_sms("Booking Rejected", self.global_mobilenum)
            return True
        else:
            raise Exception("Booking does not exist.")

    def send_sms(self, message, mobilenumber):
        # Twilio API endpoint
        url = "https://api.twilio.com/2010-04-01/Accounts/AC825fe42416c2169fc9991c0597b4a5ed/Messages.json"

        # Headers
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic QUM4MjVmZTQyNDE2YzIxNjlmYzk5OTFjMDU5N2I0YTVlZDozNjYyNjc1YzAxM2ZkMjdhYTU5ZjZjYzUzYTM1M2JhNQ==",
        }

        # Payload
        payload = {
            "Body": message,
            "To": mobilenumber,
            "From": "+447400364837",
        }

        # Make the request
        response = requests.post(url, headers=headers, data=payload)

        # Display the response
        # print("Response Code:", response.status_code)
        # print("Response Content:", response.text)
