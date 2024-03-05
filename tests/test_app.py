from playwright.sync_api import Page, expect

# Tests for your routes go here


def test_get_all_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/index")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Name: space_1",
        "Price per night: 45.51",
        "Description: description_1",
        "Name: space_2",
        "Price per night: 14000.99",
        "Description: description_2"
    ])

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