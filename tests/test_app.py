from playwright.sync_api import Page, expect

# Tests for your routes go here


def test_get_all_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/spaces")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "space_1",
        "space_2"
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