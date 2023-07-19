# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Submit message route
POST /submit
  email: string
  password: string
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE


"""
Test if the email and password doesn’t match existing database
User will able to sign up and it will redirect to index(homepage) for you to log in 
"""
# POST /submit
#  Parameters:
#    email: testname_1@example.com
#    password: testpassword
#  Expected response (200 OK):

"""
No response output
redirects to the index page
"""


# POST /submit
#  Parameters: an existing email and password
#    email: asha@example.com
#    password: password1
#  Expected response (400 Bad Request):

'''
user already exists
'''


"""
If input is none or invalid
it will ask to provide email and a password
"""
# POST /submit
#  Parameters: none / empty string
#  Expected response (400 Bad Request):
"""
Please provide a email and a password
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python


