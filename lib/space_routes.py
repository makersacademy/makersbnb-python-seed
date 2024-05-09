from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect, url_for
from lib.date import Date
from lib.space import Space
from lib.date_repository import DateRepository
from lib.space_repository import SpaceRepository
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date, timedelta

def apply_space_routes(app):

    @app.route('/spaces')
    def get_spaces():
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        spaces = space_repository.all()
        return render_template('spaces/index.html', spaces=spaces)

    @app.route('/spaces/new', methods=['GET'])
    def get_new_space():
        return render_template('spaces/new.html')
    
    @app.route('/spaces', methods=['POST'])
    def post_new_space():
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        # we need to figure out how to extract user_id from who is logged in, currently set to 1 in below line
        space_id = repository.create(request.form['name'], request.form['description'], request.form['price'], 1)

        date_repository = DateRepository(connection)
        start_date = str(request.form['start_date'])
        end_date = str(request.form['end_date'])
        date1 = date.fromisoformat(start_date)
        date2 = date.fromisoformat(end_date)
        date_diff = (date2 - date1).days
        for i in range(date_diff+1):
            new_date = Date(None, date1 + timedelta(days=i), False, space_id)
            date_repository.create(new_date)
            
        return redirect(url_for('get_spaces'))
    
    @app.route('/spaces/<space_id>', methods=['GET', 'POST'])
    def get_space(space_id):
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        space, error_message = repository.find_space_and_dates(space_id)
        if error_message == "No dates available":
            space = repository.find(space_id)
            return render_template('spaces/show.html', space=space, error = "No dates available")
        if request.method == 'POST':
            selected_date_ids = request.form.getlist('selected_date')
            if selected_date_ids == []:
                return render_template('spaces/show.html', space=space, error = "Please select at least one date")
            booking_repository = BookingRepository(connection)
            for date_id in selected_date_ids:
                booking = Booking(None, date_id, 1) #need to add session user_id 
                booking_repository.create(booking)
            return "Booking request created"
        return render_template('spaces/show.html', space=space)
    

    