from playwright.sync_api import Page, expect
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    h1_tag = page.locator("h1")
    h2_tag = page.locator("h2")
    anchor_tag = page.locator("a")

    expect(h2_tag).to_have_text("Log in")
    expect(anchor_tag).to_have_text("Sign up")
    expect(h1_tag).to_have_text("Makers BnB")
"""
We can render the sign up page
"""
def test_get_signup(page, test_web_address,db_connection):
    db_connection.seed('seeds/makers_bnb_database.sql')
    page.goto(f"http://{test_web_address}/index")
    page.click("text= Sign up")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Sign up")

"""
When user enters exisitng details it will redirect to 
back to the sign in page
"""
def test_check_existing_user(page, test_web_address,db_connection):
    db_connection.seed('seeds/makers_bnb_database.sql')
    page.goto(f"http://{test_web_address}/sign-up")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']","password1")
    page.get_by_role("button").click()
    error_element = page.locator(".sign-up-error")
    expect(error_element).to_have_text("User already exists")


"""
When new user enters details it will redirect to 
login page
"""
def test_check_for_new_user(page, test_web_address,db_connection):
    db_connection.seed('seeds/makers_bnb_database.sql')
    page.goto(f"http://{test_web_address}/sign-up")
    page.fill("input[name='email']", "steve@example.com")
    page.fill("input[name='password']","stevepassword")
    page.get_by_role("button").click()
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Log in")

"""
When new user enters invalid(empty) password it will redirect back
sign up page
"""
def test_check_for_new_user_with_invalid_password(page, test_web_address,db_connection):
    db_connection.seed('seeds/makers_bnb_database.sql')
    page.goto(f"http://{test_web_address}/sign-up")
    page.fill("input[name='email']", "bob@example.com")
    page.fill("input[name='password']","")
    page.get_by_role("button").click()
    error_element = page.locator(".password-error")
    expect(error_element).to_have_text("Password invalid")

"""
We can render the listings page
"""
def test_get_listings(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.goto(f"http://{test_web_address}/listings")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Listings")


"""
We see a list of all properties from the properties table in /listings
"""
def test_all_properties_listed_in_listings(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.goto(f"http://{test_web_address}/listings")
    list_tag = page.locator('[class="listings"]')
    expect(list_tag).to_have_text([
        "Hackers Hideaway",
        "Ma house",
        "Makers HQ"
    ])



""""
Each listing on the /listings page links to its own /listings/<id> page
"""
def test_listing_item_links_to_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.goto(f"http://{test_web_address}/listings")
    page.click("text=Ma house")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Ma house")

"""
When we click List your property /listings redirects to /list-property page
"""
def test_listings_redirects_to_list_property(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.goto(f"http://{test_web_address}/listings")
    page.click("text=List your property")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("List your property")

"""
An existing user can log in with their correct email and password
and be redirected to the /listings page
"""
def test_existing_user_log_in(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Listings")

"""
A user without an account gets an error message when they try to log in
"""
def test_non_user_log_in_error(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "notreal@example.com")
    page.fill("input[name='password']", "p@ssword")
    page.get_by_role("button").click()
    error_element = page.locator(".login-error")
    expect(error_element).to_have_text("User does not exist")

"""
When a user clicks the Sign up button they are redirected to /sign-up
"""
def test_sign_up_button_redirects(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.click("text=Sign up")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Sign up")

'''
When an existing user enters the wrong password there is an error message
'''
def test_wrong_password_by_existing_user(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "p@ssword")
    page.get_by_role("button").click()
    error_element = page.locator(".login-error")
    expect(error_element).to_have_text("Incorrect password. Please try again.")


"""
When on listings/<id> page, we see the property's short description and price per night
"""
def test_listings_id_page_has_decription_and_price(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.goto(f"http://{test_web_address}/listings/1")
    description_class = page.locator(".description")
    price_class = page.locator(".price")
    expect(description_class).to_have_text("Description: A mystery place full of bugs")
    expect(price_class).to_have_text("Price: £50.00 per night")

"""
When booking a property with available dates
BookingRepository#all returns list including the booking
and we see a "Booking Complete" message on /listings/id
"""
def test_booking_available_property_updates_db_and_confirmation_message(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "fahim@example.com")
    page.fill("input[name='password']", "password3")
    page.get_by_role("button").click()
    page.click("text=Ma house")
    page.fill("input[name='start_date']", "2024-02-17")
    page.fill("input[name='end_date']", "2024-02-18")
    page.get_by_role("button").click()
    repository = BookingRepository(db_connection)
    assert repository.all() == [
        Booking(1,date(2024, 1, 1), date(2024,1,8), 1, 4),
        Booking(2,date(2024, 2, 14), date(2024, 2,15), 2, 2),
        Booking(3,date(2024,6,7), date(2024,8,7), 3, 1),
        Booking(4,date(2024,1,10), date(2024,1,16), 1, 3),
        Booking(5,date(2024,2,17), date(2024,2,18), 2, 3)
    ]
    confirmation = page.locator(".confirmation")
    expect(confirmation).to_have_text("Booking confirmed")

"""
When booking a property that is not available for the chosen dates
we see an error message "Property booked for those dates"
""" 
def test_not_available_dates_and_property_booked_for_those_date_message(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "fahim@example.com")
    page.fill("input[name='password']", "password3")
    page.get_by_role("button").click()
    page.click("text=Ma house")
    page.fill("input[name='start_date']", "2024-02-14")
    page.fill("input[name='end_date']", "2024-02-15")
    page.get_by_role("button").click()
    repository = BookingRepository(db_connection)
    assert repository.all() == [
        Booking(1,date(2024, 1, 1), date(2024,1,8), 1, 4),
        Booking(2,date(2024, 2, 14), date(2024, 2,15), 2, 2),
        Booking(3,date(2024,6,7), date(2024,8,7), 3, 1),
        Booking(4,date(2024,1,10), date(2024,1,16), 1, 3)
    ]
    error_message = page.locator(".error")
    expect(error_message).to_have_text("Property is unavailable for those dates")

"""
When we click List your property /listings redirects to /list-property page
and then we can create a new listing that will appear on the /listings page
"""
def test_create_new_listing(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.click("text=List your property")
    page.fill("input[name='name']", "Our house")
    page.fill("input[name='description']", "In the middle of our street")
    page.fill("input[name='price']", "20.00")
    page.get_by_role("button").click()
    page.click("text=Our house")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text("Our house")

'''
when we are trying to list a property that has no price
we get an error "please fill in all the details"
'''   
def test_creating_listing_without_price(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.click("text=List your property")
    page.fill("input[name='name']", "Our house")
    page.fill("input[name='description']", "In the middle of our street")
    page.fill("input[name='price']", "")
    page.get_by_role("button").click()
    error_element = page.locator(".listing-error")
    expect(error_element).to_have_text("Please fill in all the details.")

'''
when we are trying to list a property that has no name
we get an error "please fill in all the details"
'''   
def test_creating_listing_without_name(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.click("text=List your property")
    page.fill("input[name='name']", "")
    page.fill("input[name='description']", "In the middle of our street")
    page.fill("input[name='price']", "50.00")
    page.get_by_role("button").click()
    error_element = page.locator(".listing-error")
    expect(error_element).to_have_text("Please fill in all the details.")

'''
when we are trying to list a property that has no description
we get an error "please fill in all the details"
'''   
def test_creating_listing_without_description(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.click("text=List your property")
    page.fill("input[name='name']", "Our house")
    page.fill("input[name='description']", "")
    page.fill("input[name='price']", "50.00")
    page.get_by_role("button").click()
    error_element = page.locator(".listing-error")
    expect(error_element).to_have_text("Please fill in all the details.")

'''
when you are logged user has properties 
you can see them listed in my listings page
'''
def test_get_my_listings_page_with_properties_attached(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_database.sql')
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    page.goto(f"http://{test_web_address}/my-listings")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("My listings")
    name_tag = page.locator(".name")
    expect(name_tag).to_have_text([
        "Name: Hackers Hideaway",
        "Name: Ma house"
    ]) 

'''
when you are logged user has no properties 
you will see an error message saying
"You have no listings to view"
'''
def test_get_my_properties_with_no_properties_attached(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_database.sql')
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "fahim@example.com")
    page.fill("input[name='password']", "password3")
    page.get_by_role("button").click()
    page.goto(f"http://{test_web_address}/my-listings")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("My listings")
    error_tag = page.locator(".error")
    expect(error_tag).to_have_text("You have no listings to view")
    
'''
after logging in, I want to be able to click on the navigation button "My Bookings"
and be redicted to a page where I can see all of my confirmed bookings
'''
def test_logged_in_user_can_see_my_bookings_page_with_confirmed_bookings(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "fahim@example.com")
    page.fill("input[name='password']", "password3")
    page.get_by_role("button").click()
    page.click("text=Ma house")
    page.fill("input[name='start_date']", "2024-02-17")
    page.fill("input[name='end_date']", "2024-02-18")
    page.get_by_role("button").click()
    page.click("text=My Bookings")
    my_bookings = page.locator(".my_bookings")
    expect(my_bookings).to_have_text([
        "Hackers Hideaway - 2024-01-10 - 2024-01-16",
        "Ma house - 2024-02-17 - 2024-02-18"
    ])

    """
    When booking dates are invalid, we see an error message
    """
    def test_invalid_booking_dates_generates_error(page, test_web_address, db_connection):
        db_connection.seed("seeds/makers_bnb_database.sql")
        page.goto(f"http://{test_web_address}/index")
        page.fill("input[name='email']", "fahim@example.com")
        page.fill("input[name='password']", "password3")
        page.get_by_role("button").click()
        page.click("text=Ma house")
        page.fill("input[name='start_date']", "2024-02-20")
        page.fill("input[name='end_date']", "2024-02-18")
        page.get_by_role("button").click()
        error = page.locator(".error")
        expect(error).to_have_text("Please insert: a start date that is earlier than the end date")
