from playwright.sync_api import Page, expect

def test_get_spaces(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb_seeds.sql")

    page.goto(f"{test_web_address}/spaces")
    