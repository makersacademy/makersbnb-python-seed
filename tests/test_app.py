from playwright.sync_api import Page, expect

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


# Tests for your routes go here
"""
Given there is no spaces. View spaces returns empty list.
"""
def test_when_empty_list_of_spaces():
    user = User('Adamexample@gmail.com', 'password123')
    assert user.view_spaces() == []


"""
User adds a new space and then list all the spaces. User can see that space has been added.
"""
def test_when_one_space_added():
    user = User('Adam.takac@gmail.com', 'password456!')
    user.add_space('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)
    assert user.view_spaces == ('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)

"""
User adds multiple spaces and then lists all the spaces. User can see all the added spaces.
"""
def test_when_multiple_spaces_added():
    user = User('adamtakac24@outlook.com', 'Pass123!')
    user.add_space('Cozy Cottage', 'A charming cottage in the countryside.', 120.00)
    user.add_space('Luxurious apartment', 'Stunning luxurious apartment in the city center.', 250.00)
    user.add_space('Lake District treehouse', 'Adventorous treehouse cabin located in Lake District.', 100.00)
    assert len(user.view_spaces()) == 3
    assert user.view_spaces == [
        {'name': 'Cozy Cottage', 'description': 'A charming cottage in the countryside.', 'price_per_night': 120.00},
        ['name': 'Luxurious apartment', 'description': 'Stunning luxurious apartment in the city center.', 'price_per_night': 250.00]
        ['name': 'Lake District treehouse', 'description': 'Adventorous treehouse cabin located in Lake District.','price_per_night': 100.00]
    ]

