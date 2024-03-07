import os
from playwright.sync_api import Page, expect
import pytest
import psycopg
from flask import Flask, request, render_template, redirect, url_for 
from lib.database_connection import get_flask_database_connection
import app



# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")
#     # We look at the <p> tag
#     strong_tag = page.locator("p")
#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")


# == Your Test Routes Here ==

"""
Request: GET/  (home page)
Response: this testst if the flask route works correctly and renders the right template
"""
def test_get_index_(db_connection, web_client):
    get_response = web_client.get("/")
    db_connection.seed("seeds/bnb_table.sql")
    assert get_response.status_code == 200

"""
Request: POST/  (home page)
Response: checks if the user creation behaves as expected
"""
def test_post_index(db_connection, web_client):
    db_connection.seed("seeds/bnb_table.sql")
    # Testing with valid data
    valid_post_response = web_client.post("/", data={'email': "adam.email@gmail.com", 'password': 'newpass333!', 'confirm-password': 'newpass333!'})
    # User is expected to be redirected after successful registration, hence 302 code
    assert valid_post_response.status_code in [200, 302]


    # Testing when passwords do not match
    mismatch_password_response = web_client.post("/", data={'email': "Adamexample@gmail.com", 'password': 'password123!!!', 'confirm-password': 'password456!!!'})
    assert mismatch_password_response.status_code == 200
    assert mismatch_password_response.data.decode('utf-8') == "<p>passwords do not match!</p>"


"""
Request: POST/  (home page)
Response: checks if the password is valid
"""
def test_post_index_invalid_passwords(db_connection, web_client):
    # Password too short and without special character
    response_short_no_special = web_client.post("/", data={'email': "user@example.com", 'password': 'short', 'confirm-password': 'short'})
    assert response_short_no_special.status_code == 400
    assert response_short_no_special.data.decode('utf-8') == "Password does not meet the criteria, password needs to be 8 characters long and contain a special character" 


    # Password long enough but without special character
    response_no_special = web_client.post("/", data={'email': "user@example.com", 'password': 'longpassword', 'confirm-password': 'longpassword'})
    assert response_no_special.status_code == 400
    assert response_no_special.data.decode('utf-8') == "Password does not meet the criteria, password needs to be 8 characters long and contain a special character" 

    # Password with special character but too short
    response_short_with_special = web_client.post("/", data={'email': "user@example.com", 'password': 'short!', 'confirm-password': 'short!'})
    assert response_short_with_special.status_code == 400
    assert response_short_with_special.data.decode('utf-8') == "Password does not meet the criteria, password needs to be 8 characters long and contain a special character"











# """
# Testing client side functionality - web page design
# """
# def test_signup_form_elements(page):
#     # Navigate to the web page
#     page.goto('http://localhost:5000/')

#     # Test that username input is there
#     username_input = page.locator("input[name='username']")
#     expect(username_input).to_be_visible()
#     expect(username_input).to_have_attribute("type", "text")


#     # Test that username input is there
#     username_input = page.locator("input[name='password']")
#     expect(username_input).to_be_visible()
#     expect(username_input).to_have_attribute("type", "password")

















# # Tests for your routes go here
# """
# Given there is no spaces. View spaces returns empty list.
# """
# def test_when_empty_list_of_spaces():
#     user = User('Adamexample@gmail.com', 'password123')
#     assert user.view_spaces() == []


# """
# User adds a new space and then list all the spaces. User can see that space has been added.
# """
# def test_when_one_space_added():
#     user = User('Adam.takac@gmail.com', 'password456!')
#     user.add_space('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)
#     assert user.view_spaces == ('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)

# """
# User adds multiple spaces and then lists all the spaces. User can see all the added spaces.
# """
# def test_when_multiple_spaces_added():
#     user = User('adamtakac24@outlook.com', 'Pass123!')
#     user.add_space('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)
#     user.add_space('Luxurious apartment', 'Stunning luxurious apartment in the city center.', 250.00)
#     user.add_space('Lake District treehouse', 'Adventorous treehouse cabin located in Lake District.', 100.00)
#     assert len(user.view_spaces()) == 3
#     assert user.view_spaces == [
#         {'name': 'Cozy Cottage', 'description': 'A charming cottage in the countryside.', 'price_per_night': 120.00},
#         ['name': 'Luxurious apartment', 'description': 'Stunning luxurious apartment in the city center.', 'price_per_night': 250.00]
#         ['name': 'Lake District treehouse', 'description': 'Adventorous treehouse cabin located in Lake District.','price_per_night': 100.00]
#     ]

