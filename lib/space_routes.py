from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect, url_for
from lib.date import Date
from lib.space import Space
from lib.date_repository import DateRepository
from lib.space_repository import SpaceRepository

def apply_space_routes(app):

    @app.route('/spaces')
    def get_spaces():
        connection = get_flask_database_connection()
        space_repository = SpaceRepository(connection)
        spaces = space_repository.all()
        return render_template('spaces.html', spaces=spaces)

    # @app.route('/spaces/<space_id>')
    # def get_space(space_id):
    #     connection = get_flask_database_connection()
    #     space_repository = SpaceRepository(connection)
    #     date_repository = DateRepository(connection)
    #     space = space_repository.find(space_id)
    #     dates = date_repository.get_by_space_id(space_id)
    #     return render_template('space.html', space=space, dates=dates)

    # @app.route('/spaces/<space_id>/dates', methods=['POST'])
    # def add_date(space_id):
    #     connection = get_flask_database_connection()
    #     date_repository = DateRepository(connection)
    #     date = Date(request.form['date'], space_id)
    #     date_repository.add(date)
    #     return redirect(url_for('space', space_id=space_id))

    # @app.route('/spaces/<space_id>/dates/<date_id>', methods=['POST'])
    # def delete_date(space_id, date_id):
    #     connection = get_flask_database_connection()
    #     date_repository = DateRepository(connection)
    #     date_repository.delete(date_id)
    #     return redirect(url_for('space', space_id=space_id))

    # @app.route('/spaces/<space_id>/dates/<date_id>/edit', methods=['POST'])
    # def edit_date(space_id, date_id):
    #     connection = get_flask_database_connection()
    #     date_repository = DateRepository(connection)
    #     date = Date(request.form['date'], space_id)
    #     date.id = date_id
    #     date_repository.update(date)
    #     return redirect(url_for('space', space_id=space_id))

    # @app.route('/spaces/<space_id>/dates/<date_id>/edit')
    # def edit_date_form(space_id, date_id):
    #     connection = get_flask_database_connection()
    #     date_repository = DateRepository(connection)
    #     date = date_repository.get_by_id(date_id)
    #     return render_template('edit_date.html', date=date)

    # @app.route('/spaces/<space_id>/dates/<date_id>/delete')
    # def delete_date_form(space_id, date_id):
    #     connection = get_flask_database_connection()
    #     date_repository = DateRepository(connection)
    #     date = date_repository.get_by_id(date_id)
    #     return render_template('delete_date.html', date=date)

    