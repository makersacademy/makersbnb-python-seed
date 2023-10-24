from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")

def test_get_spaces(page, test_web_address):

    page.goto(f"http://{test_web_address}/spaces")

    heading = page.locator("h1")
    expect(heading).to_have_text("Book a space")

    button = page.locator('button')
    expect(button).to_have_text("List a space")

    listings = page.locator('li')
    expect(listings).to_have_text([
        'Cozy Cottage\nA charming cottage for a peaceful retreat',
        'Beachfront Villa\nEnjoy stunning ocean views in this luxury villa',
        'Mountain Chalet\nExperience the beauty of the mountains in this cozy chalet',
        'City Apartment\nConvenient urban living in the heart of the city',
        'Lakefront Cabin\nRustic cabin on the tranquil shores of the lake',
        'Seaside Bungalow\nRelax in a charming bungalow by the sea',
        'Luxury Resort Suite\nIndulge in luxury at this 5-star resort suite',
        'Countryside Retreat\nEscape to the peaceful countryside in this cottage',
        'Historic Mansion\nStep back in time at this historic mansion',
        'Riverside Cabin\nCozy cabin with a river view, perfect for fishing',
    ])

def test_get_new(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/spaces/new")

    # We look at the <p> tag
    heading = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(heading).to_have_text("List a space")

