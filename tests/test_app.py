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

def test_signup_successful(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")

    # Fill out the signup form
    page.fill('input[name="first_name"]', 'John')
    page.fill('input[name="last_name"]', 'Doe')
    page.fill('input[name="email"]', 'john.doe@example.com')
    page.fill('input[name="phone_number"]', '1234567890')
    page.fill('input[name="username"]', 'testuser')
    page.fill('input[name="password"]', 'testpassword')

    # Click the "Sign Up" button
    page.click("text=Sign Up")

    # Wait for an element indicating successful signup
    success_message = page.locator('body:has-text("Sign-up successful!")')
    success_message.wait_for_timeout(timeout=5000)

    # Assert that the success message is visible
    assert success_message.is_visible()