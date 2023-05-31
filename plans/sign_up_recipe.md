**Title:** 
<br>User Registration

**User Story:**
<br>As a potential user of the BnB site, I want to be able to register for an account so that I can access personalized features and interact with the platform.

**Acceptance Criteria:**
1. As a new user, I should be able to access the registration page.
2. On the registration page, I should see fields to enter my name, email address, password, and other required details.
3. After filling in the registration form, I should be able to submit it.
4. If the registration is successful, I should receive a confirmation message and be redirected to the login page.

**Database Design:**
Table name: users
Parameters: id, name, username, password, email

```sql
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT,
    password TEXT
);
```

**Classes:**
User
    Constructor
UserRepository
    Add
    Get by username
    Get by email
    Check username is unique
    Check email is unique


**App.py Methods**
1. GET the sign up page
```python
@app.route('/signup')
def get_signup():
    return render_template('sign_up.html')
```

2. POST the form submission
    -- Check that username and email are unique
    -- Check that password and confirm password are identical
```python
def password_is_valid(password):
    special_char = "!@#$%^&*()-_=+[]{};:,<.>/?`~"
    return len(password) > 8 and any(char in special_char for char in password)

@app.route('/signup', methods=['POST'])
def add_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    user_created = False

    # User submits information
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Error message if email address is in database
    if not repository.email_is_unique(email):
        error_message = "Email address is already registered"
        return render_template('sign_up.html', error_message=error_message)

    # Error message if username already exists
    if not repository.username_is_unique(username):
        error_message = "Username already taken"
        return render_template('sign_up.html', error_message=error_message)

    # Error message if password is not valid


    user = User(None, name, username, email, password)
    repository.add(user)

    user_created = True

    return render_template('sign_up.html', user_created=user_created)
```


**UserRepository Methods**
```python
'''
Check if username is already in the users table
'''
def username_is_unique(self, username):
    # Count the number of times the username is in the database
    query = "SELECT COUNT(*) FROM users WHERE username = %s"
    count = self._connection.execute(query, [username])
    if count == 0:
        return True

'''
Check if email is already in the users table
'''
def email_is_unique():
    # Count the number of times the email is in the database
    query = "SELECT COUNT(*) FROM users WHERE email = %s"
    count = self._connection.execute(query, [email])
    if count == 0:
        return True
```