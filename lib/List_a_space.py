# from flask import Flask, render_template, request, redirect
# from lib.database_connection import get_flask_database_connection
# from datetime import datetime 

# app = Flask(__name__) 

# listings = []

# @app.route('/listings/new', methods = ['POST'])
# def create_listing():
#     if request.method == "POST":
#         title = request.form['Name']
#         description = request.form['Description']
#         price_per_night = request.form['Price_per_night']
#         available_from = datetime.strftime(request.form['available_from'], '%d/%m/%y').date()
#         available_to = datetime.strftime(request.form['available_to'], '%d/%m/%y').date() 


#     new_listing = {
#         'title' : title,
#         'description' : description,
#         'price_per_night' : price_per_night,
#         'available_from' : available_from,
#         'available_to' : available_to
#     }

#     listings.append(new_listing) 


# # now = datetime.now()
# #formatted_date = now.strftime("%d-%m-%Y") Y = 2023 y = 23, 30/05/2023

