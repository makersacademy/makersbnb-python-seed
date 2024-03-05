import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))




# == Your Routes Here ==
    def add_space(self, name, description, price_per_night):
        new_space = {
            'name': name,
            'description': description,
            'price_per_night': price_per_night
        }
        self.spaces.append(new_space)

    def view_spaces(self):
        return self.spaces

    def request_rental(self, space_id, date):
        # Parameters:
        #   space_id: int
        #   date: Date
        # Returns:
        #   Nothing. Creates a booking request in database for that specific date
        pass # No code here yet

    def check_status(self, booking_id):
        # Parameters:
        #   booking_id: int
        # Returns:
        #   Returns the current status of the booking
        pass # No code here yet

    def respond(self, booking_id, respond):
        # Parameters:
        #   booking_id: int
        #   response: string
        # Returns:
        #   Updates the status of booking in database based on the respond
        pass # No code here yet

