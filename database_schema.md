## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a potential user of the BnB site, I want to be able to register for an account so that I can access personalized features and interact with the platform.

As a registered user of the BnB site, I want to be able to create a listing for my property so that I can start offering it to potential guests.

As a user of the BnB site, I want to be able to log in to my account so that I can access my personalized features and interact with the platform.

As a logged-in user of the BnB site, I want to be able to browse available listings and book a space for my desired dates and number of guests.


```

```
Nouns:

user, space, booking, date, guests, price, location, availability, description, email, password, name, username, total

```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| listings              | price, location, availability, description    |
| users                 | email, password, username                     |
| bookings              | guests, date, total                           |

Name of the table (always plural): `listings`, `users`, `bookings`

## 3. Decide the column types

Column names: `price`, `location`, `password`, `username`, `availability`, `description`, 
`guests`, `date`

## 4. Write the SQL

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE,
    password VARCHAR(64),
    email VARCHAR(20)
);

CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    price FLOAT,
    location VARCHAR(20),
    description TEXT,
    availability BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    listing_id INTEGER,
    total FLOAT,
    start_date DATE,
    end_date DATE,
    confirmed BOOLEAN,
    FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

```

## 5. Create the table

```bash
psql -h 127.0.0.1 makersbnb < makersbnb.sql
```

## 6. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Home route
GET /

```

## 7. Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

## 7.1 Unit Testing

```python
"""
Listing constructs with a price, location, availability, description and user_id
"""
def test_listing_constructs():
    listing = Listing(1, 150, True, "listing description", 1)
    assert listing.id == 1
    assert listing.price == 150
    assert listing.availability == True
    assert listing.description == "listing description"
    assert listing.user_id == 1

"""
We can format listings to strings nicely
"""
def test_listings_format_nicely():
    listing = Listing(1, 150, True, "listing description", 1)
    assert str(listing) == "Listing(id=1, price=150, availability=True, description='listing description', user_id=1)"

"""
We can compare two identical listings
And have them be equal
"""
def test_listings_are_equal():
    listing_1 = Listing(1, 150, True, "listing description", 1)
    listing_2 = Listing(1, 150, True, "listing description", 1)
    assert listing_1 == listing_2
```

## 7.2 Database Testing

```python
"""
When we click on homepage, we
get all listings
"""
def test_db_list_all_listings(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = ListingRepository(db_connection)

    result = repository.all()
    assert result == [
        Listing(1, 150, "listing description", 1),
        Listing(2, 300, "listing description", 1)
    ]
```

## 7.3 Route Testing

```python
"""
# GET /
#  Expected response (200 OK):
"""

def test_get_homepage(web_client):
    response = web_client.get('/')
    assert response.status_code == 200

```

## 7.4 End to End/Integration Testing
```python
"""
As a signed out or signed in User
When I visit the homepage
I see all listings available to book
I see the option to sign in and sign up
"""

def test_homepage_see_all_listings(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/")
    listing = page.locator('.listing-description')
    assert listing.inner_text() == "listing description"
```

## 8. Decide on The Tables Relationship

1. Can one user own many listings? YES
2. Can one listing have many users? NO

-> Therefore,
-> A user HAS MANY listings
-> An listing BELONGS TO a user

-> Therefore, the foreign key is on the listings table.


## 9. Design the Many-to-Many relationship

1. Can one user book many listings? YES
2. Can one listing be booked by many users? YES

-> Therefore we need a joins table
-> Join table name: bookings
-> Columns: user_id, listing_id
