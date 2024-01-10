import pytest
from playwright.sync_api import Page, expect

"""
We can render a bookings index page
"""
def test_get_bookings(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/bookings")
    label_tags = page.locator("label").all()
    expect(label_tags[0]).to_have_attribute("for", "id")
    assert label_tags[0].inner_text() == "Space ID:"

"""
We can navigate to the booking page for a given space using /bookings POST
"""
def test_post_bookings(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/bookings")
    page.get_by_label("Space ID:").fill("1")
    page.get_by_role("button").click()
    expect(page).to_have_url(f"http://{test_web_address}/bookings/new/1")

"""
We can render a page for creating new bookings
"""
@pytest.mark.skip(reason="Test not written")
def test_get_bookings_new(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/bookings/new/1")

"""
We can create a new booking using the new booking form
"""
@pytest.mark.skip(reason="Test not written")
def test_post_bookings_new(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/bookings/new")

"""
An error is generated if an attempt is made to book an unavailable date
"""
@pytest.mark.skip(reason="Test not written")
def test_post_bookings_new(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/bookings/new")