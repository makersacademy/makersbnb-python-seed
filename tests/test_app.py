from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("Sign Up")


# def test_get_spaces(page, test_web_address):

#     page.goto(f"http://{test_web_address}/spaces")

#     heading = page.locator("h1")
#     expect(heading).to_have_text("Book a space")

#     button = page.locator('button')
#     expect(button).to_have_text("List a space")

#     listings = page.locator('li')
#     expect(listings).to_have_text([
#         'Cozy Cottage\nA charming cottage for a peaceful retreat',
#         'Beachfront Villa\nEnjoy stunning ocean views in this luxury villa',
#         'Mountain Chalet\nExperience the beauty of the mountains in this cozy chalet',
#         'City Apartment\nConvenient urban living in the heart of the city',
#         'Lakefront Cabin\nRustic cabin on the tranquil shores of the lake',
#         'Seaside Bungalow\nRelax in a charming bungalow by the sea',
#         'Luxury Resort Suite\nIndulge in luxury at this 5-star resort suite',
#         'Countryside Retreat\nEscape to the peaceful countryside in this cottage',
#         'Historic Mansion\nStep back in time at this historic mansion',
#         'Riverside Cabin\nCozy cabin with a river view, perfect for fishing',
#     ])

# def test_get_new(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/spaces/new")

#     # We look at the <p> tag
#     heading = page.locator("h1")

#     # We assert that it has the text "This is the homepage."
#     expect(heading).to_have_text("List a space")

def test_create_listing(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb.sql")
    page.goto(f"http://{test_web_address}/spaces")

    # This time we click the link with the text 'Add a new book'
    page.click("text=List a space")

    # Then we fill out the field with the name attribute 'title'
    page.fill("input[name='name']", "The Hobbit")

    # And the field with the name attribute 'author_name'
    page.fill("input[name='description']", "J.R.R. Tolkien")

    page.fill("input[name='price']", "11.99")

    page.fill("input[name='user_id']", "1")

    # Finally we click the button with the text 'Create Book'
    page.click("text=List my space")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    title_element = page.locator("h1")
    expect(title_element).to_have_text("Book a space")

   
    # We assert that it has the text "This is the homepage."
    expect(heading).to_have_text("Book a space")

def test_signup_user(db_connection, page, test_web_address):
    db_connection.seed('seeds/bnb.sql')
    page.goto(f"http://{test_web_address}/index")

    page.fill("input[name='username']", "testuser")
    page.fill("input[name='email']", "testuser@email.com")
    page.fill("input[name='password']", "testpassword")

    page.click("text=Sign Up")

