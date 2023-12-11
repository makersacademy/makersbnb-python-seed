# Makers BnB Route Design Recipe


## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Home route
GET /home

<!-- # Waving route
GET /wave?name=<string> -->

# Submit message route
POST /space
  name: string
  description: string
  price: integer

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /spaces
#  Expected response (200 OK):
"""
Bagend, hobbit hole, 50
"""


# POST /spaces
#  Parameters:
#      name: Bagend
#      description: Hobbit hole
#      price: 50
#  Expected response (200 OK):
"""
Bagend, hobbit hole, 50
"""

# POST /spaces
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /spaces
  Expected response (200 OK):
  "Bagend, hobbit hole, 50"

  And any other listings that have been posted
"""
def test_get_spaces(web_client):
    response = web_client.get('/spaces')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Bagend, hobbit hole, 50'

"""
POST /space
  Parameters:
    name: Bagend
    description: Hobbit hole
    price: 50
  Expected response (200 OK):
  "'Thanks, you posted your space'""
"""
def test_post_submit(web_client):
    response = web_client.post('/space', data={'name': 'Bagend', 'description': 'Hobbit hole', 'price': '50'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks, you posted your space'
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->