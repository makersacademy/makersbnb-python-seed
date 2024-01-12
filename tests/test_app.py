from playwright.sync_api import Page, expect
from flask import session
# Tests for your routes go here

"""
We can render the index page
"""

def test_get_homepage_redirects(page, test_web_address,web_client):
    response = web_client.get('/')
    assert response.status_code ==302
    page.goto(f'http://{test_web_address}/')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Space Listings')
def test_get_index(page, test_web_address,web_client):
    response = web_client.get('/index')
    assert response.status_code == 200
    assert 'Welcome to MakersBnB' in response.data.decode('utf-8')

    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")
    
    # We look at the <p> tag
    strong_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."

    expect(strong_tag).to_have_text("Welcome to MakersBnB")
# test

"""
We can render the login page
"""

def test_get_login(page, test_web_address,web_client):
    page.goto(f"http://{test_web_address}/log_in")
    response = web_client.get('/log_in')
    assert response.status_code == 200
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("Please log in.")

def test_post_login(page,test_web_address,web_client):
    response = web_client.post('/log_in', data={'email':'user_1@mail.com','passw':'makersbnb2'})
    assert response.status_code == 302
    assert 'Redirecting' in response.data.decode('utf-8')
    response = web_client.post('/log_in', data={'email':'user_@mail.com','passw':'makersbnb2'})
    assert response.status_code == 200
    assert 'Email or password is incorrect.' in response.data.decode('utf-8')
    page.goto(f"http://{test_web_address}/log_in")
    page.fill('input[name=email]','user_1@mail.com')
    page.fill('input[name=passw]','makersbnb2')
    page.click('text=Submit')
    logged_in = page.locator('.t-current_user')
    expect(logged_in).to_have_text('Signed in as user_1@mail.com')

def test_get_add_spaces(page, test_web_address,db_connection,web_client):
    db_connection.seed("seeds/MasterTest.sql")
    page.goto(f"http://{test_web_address}/index")
    
    # Then we fill out the field with the name attribute 'email'
    page.fill("input[name='email']", "test_user@mail.com")
    
    # And the field with the name attribute 'passw'
    page.fill("input[name='passw']", "testpassword123")

    page.fill("input[name='passw_conf']", "testpassword123")
    
    page.click("text=Submit")
    
    page.click('text=List new space')
    strong_tag = page.locator("h1")
    
    expect(strong_tag).to_have_text("Create new listing")
    
    response = web_client.get('/newspace')
    assert response.status_code == 302

def test_list_spaces(page,test_web_address,db_connection,web_client):
    db_connection.seed("seeds/MasterTest.sql")
    page.goto(f"http://{test_web_address}/spaces")
    h3_tag = page.locator('h3')
    expect(h3_tag).to_have_count(5)
    response = web_client.get('/spaces')
    assert response.status_code == 200
    
def test_adding_a_space(page,test_web_address,db_connection,web_client):
    db_connection.seed("seeds/MasterTest.sql")
    page.goto(f"http://{test_web_address}/index")
    # Then we fill out the field with the name attribute 'email'
    page.fill("input[name='email']", "test_user@mail.com")
    # And the field with the name attribute 'passw'
    page.fill("input[name='passw']", "testpassword123")
    page.fill("input[name='passw_conf']", "testpassword123")
    page.click("text=Submit")
    page.click('text=List new space')
    page.fill('input[name=title]','Test Title6')
    page.fill('input[name=space_desc]','This is some description')
    page.fill('input[name=price]','1.234')
    page.fill('input[name=startdate]','2024-01-17')
    page.fill('input[name=enddate]','2024-01-31')
    page.click('text=Submit')
    page.click('text=Spaces')
    h3_tag = page.locator('h3')
    expect(h3_tag).to_have_count(6)
    response = web_client.post('/newspace', data={'title':'Test','space_desc':'Test','price':'1.23','startdate':'2024-01-20','enddate':'2024-01-31'})
    assert response.status_code ==302
    response = web_client.post('/newspace', data={'title':'','space_desc':'Test','price':'1.23','startdate':'2024-01-20','enddate':'2024-01-19'})
    assert response.status_code ==200
    response = web_client.post('/newspace', data={'title':'','space_desc':'Test','price':'1.23f','startdate':'2024-01-20','enddate':'2024-01-ab'})
    assert response.status_code ==200
def test_create_user(db_connection, page, test_web_address,web_client):
    db_connection.seed("seeds/MasterTest.sql")
    
    response = web_client.post('/signup', data={'email':'testemail@mail.com','passw':'testpass','passw_conf':'testpass'})
    assert response.status_code == 302

    page.goto(f"http://{test_web_address}/index")
    
    # Then we fill out the field with the name attribute 'email'
    page.fill("input[name='email']", "test_user@mail.com")
    
    # And the field with the name attribute 'passw'
    page.fill("input[name='passw']", "testpassword123")

    page.fill("input[name='passw_conf']", "testpassword123")
    
    page.click("text=Submit")
    
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("Space Listings")

def test_create_user_wrong_pass(page,db_connection, test_web_address,web_client):
    db_connection.seed("seeds/MasterTest.sql")
    page.goto(f"http://{test_web_address}/index")
    
    # Then we fill out the field with the name attribute 'email'
    page.fill("input[name='email']", "test_user@mail.com")
    
    # And the field with the name attribute 'passw'
    page.fill("input[name='passw']", "testpassword123")

    page.fill("input[name='passw_conf']", "estpassword123")
    
    page.click("text=Submit")
    
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Welcome to MakersBnB')
    response = web_client.post('/signup', data={'email':'testemail@mail.com','passw':'estpass','passw_conf':'testpass'})
    assert response.status_code == 302
    response = web_client.post('/signup', data={'email':'user_1@mail.com','passw':'testpass','passw_conf':'testpass'})
    assert response.status_code == 302

def test_get_dashboard(page,db_connection,test_web_address,web_client):
    response = web_client.get('/dashboard')
    assert response.status_code == 302

def test_sign_out_response(web_client):
    response = web_client.get('/sign_out')
    assert response.status_code == 302

def test_requestspace_returns_page(web_client):
    response = web_client.get('/requestspace/1')
    assert response.status_code == 200