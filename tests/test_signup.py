from playwright.sync_api import Page, expect

def test_user_login(self):
    # Provide user login credentials
    login_data = {
        'email': 'john@example.com',
        'password': 'password123',
    }
    response = #.login_user(login_data) 
    
    # Assert that the login was successful
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json()['success'], True)
    self.assertEqual(response.json()['message'], 'Login successful')

def test_user_login_incorrect_credentials(self):
    # Provide incorrect user login credentials
    login_data = {
        'email': 'john@example.com',
        'password': 'wrongpassword',
    }
    response = #.login_user(login_data)
    
    # Assert that the login failed with incorrect credentials
    self.assertEqual(response.status_code, 401)
    self.assertEqual(response.json()['success'], False)
    self.assertEqual(response.json()['message'], 'Incorrect email or password')

def test_password_reset(self):
    # Provide user email for password reset
    reset_data = {
        'email': 'john@example.com',
    }
    response = #.reset_password(reset_data)
    
    # Assert that the password reset request was successful
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json()['success'], True)
    self.assertEqual(response.json()['message'], 'Password reset email sent')