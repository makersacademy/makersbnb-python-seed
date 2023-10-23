from playwright.sync_api import Page, expect

# Tests for your routes go here
"""
we want to render the spaces page
"""
def test_get_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces") 
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Spaces available.")




"""
we want to tests for lists of spaces available
"""
def test_get_list_of_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces") 
    li_tags = page.locator("li")
    expect(li_tags).to_have_text(["Sunny Cottage","Hill House","MCdonalds"])



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
    
    
    
""" we want to render add new space page """
def test_add_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/add_space")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Add a new space.")
